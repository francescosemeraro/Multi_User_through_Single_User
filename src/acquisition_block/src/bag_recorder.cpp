#include <rclcpp/rclcpp.hpp>
#include <rcpputils/filesystem_helper.hpp>
#include <std_msgs/msg/string.hpp>
#include <std_msgs/msg/int64.hpp>
#include <sensor_msgs/msg/image.hpp>
#include <visualization_msgs/msg/marker_array.hpp>

#include <rosbag2_cpp/typesupport_helpers.hpp>
#include <rosbag2_cpp/writer.hpp>
#include <rosbag2_cpp/writers/sequential_writer.hpp>
#include <rosbag2_storage/serialized_bag_message.hpp>
#include <rosbag2_compression/sequential_compression_writer.hpp>
#include <rosbag2_compression/compression_options.hpp>

using std::placeholders::_1;

class SimpleBagRecorder : public rclcpp::Node
{
public:
  SimpleBagRecorder()
  : Node("simple_bag_recorder")
  {
    bool status = rcpputils::fs::create_directories(rcpputils::fs::path("src/acquisition_block/"+ tag + "_" + info + "/"));

    if (status){

      rosbag2_compression::CompressionOptions compression_options{"zstd",rosbag2_compression::CompressionMode::FILE};
      const rosbag2_cpp::StorageOptions storage_options({("src/acquisition_block/" + tag + "_" + info).c_str(), "sqlite3"});
      const rosbag2_cpp::ConverterOptions converter_options(
        {rmw_get_serialization_format(),
        rmw_get_serialization_format()});
      
      writer_ = std::make_unique<rosbag2_cpp::Writer>(
        std::make_unique<rosbag2_compression::SequentialCompressionWriter>(compression_options));
      //writer_ = std::make_unique<rosbag2_cpp::Writer>(compressor_);

      //compressor_->open(storage_options, converter_options);
      writer_->open(storage_options, converter_options);


      if (info == "video" || info == "depth")
      {
        writer_->create_topic(
        {topic_name.c_str(),
        "sensor_msgs/msg/Image",
        rmw_get_serialization_format(),
        ""});
        
        subscription_ = create_subscription<sensor_msgs::msg::Image>(
          "/"+topic_name, 10, std::bind(&SimpleBagRecorder::topic_callback, this, _1));
      }
      else if (info == "skeleton")
      {
        writer_->create_topic(
        {topic_name.c_str(),
        "visualization_msgs/msg/MarkerArray",
        rmw_get_serialization_format(),
        ""});

        subscription_ = create_subscription<visualization_msgs::msg::MarkerArray>(
          "/"+topic_name, 10, std::bind(&SimpleBagRecorder::topic_callback, this, _1));
      }
      else if (info == "label")
      {
        writer_->create_topic(
        {topic_name.c_str(),
        "std_msgs/msg/Int64",
        rmw_get_serialization_format(),
        ""});

        subscription_ = create_subscription<std_msgs::msg::Int64>(
          "/"+topic_name, 10, std::bind(&SimpleBagRecorder::topic_callback, this, _1));
      }
      else
      {
        RCLCPP_INFO(this->get_logger(), "No subscriptions to topic, nothing being registered!");
      }

    }
  }

private:
  void topic_callback(std::shared_ptr<rclcpp::SerializedMessage> msg) const
  {
    auto bag_message = std::make_shared<rosbag2_storage::SerializedBagMessage>();

    bag_message->serialized_data = std::shared_ptr<rcutils_uint8_array_t>(
      new rcutils_uint8_array_t,
      [this](rcutils_uint8_array_t *msg) {
        auto fini_return = rcutils_uint8_array_fini(msg);
        delete msg;
        if (fini_return != RCUTILS_RET_OK) {
          RCLCPP_ERROR(get_logger(),
            "Failed to destroy serialized message %s", rcutils_get_error_string().str);
        }
      });
    *bag_message->serialized_data = msg->release_rcl_serialized_message();

    bag_message->topic_name = topic_name;
    if (rcutils_system_time_now(&bag_message->time_stamp) != RCUTILS_RET_OK) {
      RCLCPP_ERROR(get_logger(), "Error getting current time: %s",
        rcutils_get_error_string().str);
    }

    writer_->write(bag_message);
  }

  std::string info = this->declare_parameter("type_of_file","video");
  std::string tag = this->declare_parameter("tag","subject");
  std::string topic_name = this->declare_parameter("topic_name","rgb/image_raw");

  rclcpp::Subscription<rclcpp::SerializedMessage>::SharedPtr subscription_;
  std::unique_ptr<rosbag2_cpp::Writer> writer_;
  //std::unique_ptr<rosbag2_compression::SequentialCompressionWriter> compressor_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<SimpleBagRecorder>());
  rclcpp::shutdown();
  return 0;
}
