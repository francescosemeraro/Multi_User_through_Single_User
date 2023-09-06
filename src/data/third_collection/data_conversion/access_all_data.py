import sqlite3
from rosidl_runtime_py.utilities import get_message
from rclpy.serialization import deserialize_message

import matplotlib.pyplot as plt
import csv

class BagFileParser():
    def __init__(self, bag_file):
        self.conn = sqlite3.connect(bag_file)
        self.cursor = self.conn.cursor()

        ## create a message type map
        topics_data = self.cursor.execute("SELECT id, name, type FROM topics").fetchall()
        self.topic_type = {name_of:type_of for id_of,name_of,type_of in topics_data}
        self.topic_id = {name_of:id_of for id_of,name_of,type_of in topics_data}
        self.topic_msg_message = {name_of:get_message(type_of) for id_of,name_of,type_of in topics_data}

    def __del__(self):
        self.conn.close()

    # Return [(timestamp0, message0), (timestamp1, message1), ...]
    def get_messages(self, topic_name):

        topic_id = self.topic_id[topic_name]
        # Get from the db
        rows = self.cursor.execute("SELECT timestamp, data FROM messages WHERE topic_id = {}".format(topic_id)).fetchall()
        # Deserialise all and timestamp them
        return [ (timestamp,deserialize_message(data, self.topic_msg_message[topic_name])) for timestamp,data in rows]



if __name__ == "__main__":

    tags = ['s1_s2_r1_p1_s1_','s1_s2_r1_p1_s2_','s1_s2_r1_p2_s1_','s1_s2_r1_p2_s2_',
        's1_s2_r2_p1_s1_','s1_s2_r2_p1_s2_','s1_s2_r2_p2_s1_','s1_s2_r2_p2_s2_',
        's1_s3_r1_p1_s1_','s1_s3_r1_p1_s2_','s1_s3_r1_p2_s1_','s1_s3_r1_p2_s2_',
        's1_s3_r2_p1_s1_','s1_s3_r2_p1_s2_','s1_s3_r2_p2_s1_','s1_s3_r2_p2_s2_',
        's3_s2_r1_p1_s1_','s3_s2_r1_p1_s2_','s3_s2_r1_p2_s1_','s3_s2_r1_p2_s2_',
        's3_s2_r2_p1_s1_','s3_s2_r2_p1_s2_','s3_s2_r2_p2_s1_','s3_s2_r2_p2_s2_']
        
    data_type = ['skeleton','label']

    preprocess_data = False

    full_tags = []

    for j in tags:
        if j == 's1_s3_r1_p2_s2_' or j == 's1_s3_r2_p2_s1_':
            continue
        else:

            parser1 = BagFileParser("src/data/third_collection/db3/test_pairs_" + j + data_type[0] + '.db3')
            parser2 = BagFileParser("src/data/third_collection/db3/test_pairs_" + j + data_type[1] + '.db3')

            if preprocess_data:
                new_file = "src/data/third_collection/prep/" + j + 'datastream_prep.csv'
            else:
                new_file = "src/data/third_collection/csv/" + j + 'datastream.csv'

            with open(new_file, 'w', encoding='UTF8') as f:
                writer = csv.writer(f)

                skeletons = parser1.get_messages("body_tracking_data") 
                labels = parser2.get_messages("label")

                for k in range(len(labels)):
                
                    try:

                        skeleton = skeletons[k][1]
                        label = labels[k][1].data

                        # write the header
                        if preprocess_data:
                            writer.writerow([skeleton.markers[0].pose.orientation.x,skeleton.markers[0].pose.orientation.y,skeleton.markers[0].pose.orientation.z,skeleton.markers[0].pose.orientation.w,skeleton.markers[0].id,label])   
                            writer.writerow([skeleton.markers[1].pose.orientation.x,skeleton.markers[1].pose.orientation.y,skeleton.markers[1].pose.orientation.z,skeleton.markers[1].pose.orientation.w,skeleton.markers[1].id,label])   
                            writer.writerow([skeleton.markers[2].pose.orientation.x,skeleton.markers[2].pose.orientation.y,skeleton.markers[2].pose.orientation.z,skeleton.markers[2].pose.orientation.w,skeleton.markers[2].id,label])   
                            writer.writerow([skeleton.markers[3].pose.orientation.x,skeleton.markers[3].pose.orientation.y,skeleton.markers[3].pose.orientation.z,skeleton.markers[3].pose.orientation.w,skeleton.markers[3].id,label])   
                            writer.writerow([skeleton.markers[4].pose.orientation.x,skeleton.markers[4].pose.orientation.y,skeleton.markers[4].pose.orientation.z,skeleton.markers[4].pose.orientation.w,skeleton.markers[4].id,label])   
                            writer.writerow([skeleton.markers[5].pose.orientation.x,skeleton.markers[5].pose.orientation.y,skeleton.markers[5].pose.orientation.z,skeleton.markers[5].pose.orientation.w,skeleton.markers[5].id,label])   
                            writer.writerow([skeleton.markers[6].pose.orientation.x,skeleton.markers[6].pose.orientation.y,skeleton.markers[6].pose.orientation.z,skeleton.markers[6].pose.orientation.w,skeleton.markers[6].id,label])   
                            writer.writerow([skeleton.markers[7].pose.orientation.x,skeleton.markers[7].pose.orientation.y,skeleton.markers[7].pose.orientation.z,skeleton.markers[7].pose.orientation.w,skeleton.markers[7].id,label])   
                            writer.writerow([skeleton.markers[8].pose.orientation.x,skeleton.markers[8].pose.orientation.y,skeleton.markers[8].pose.orientation.z,skeleton.markers[8].pose.orientation.w,skeleton.markers[8].id,label])   
                            writer.writerow([skeleton.markers[9].pose.orientation.x,skeleton.markers[9].pose.orientation.y,skeleton.markers[9].pose.orientation.z,skeleton.markers[9].pose.orientation.w,skeleton.markers[9].id,label])   
                            writer.writerow([skeleton.markers[10].pose.orientation.x,skeleton.markers[10].pose.orientation.y,skeleton.markers[10].pose.orientation.z,skeleton.markers[10].pose.orientation.w,skeleton.markers[10].id,label])   
                            writer.writerow([skeleton.markers[11].pose.orientation.x,skeleton.markers[11].pose.orientation.y,skeleton.markers[11].pose.orientation.z,skeleton.markers[11].pose.orientation.w,skeleton.markers[11].id,label])   
                            writer.writerow([skeleton.markers[12].pose.orientation.x,skeleton.markers[12].pose.orientation.y,skeleton.markers[12].pose.orientation.z,skeleton.markers[12].pose.orientation.w,skeleton.markers[12].id,label])   
                            writer.writerow([skeleton.markers[13].pose.orientation.x,skeleton.markers[13].pose.orientation.y,skeleton.markers[13].pose.orientation.z,skeleton.markers[13].pose.orientation.w,skeleton.markers[13].id,label])   
                            writer.writerow([skeleton.markers[14].pose.orientation.x,skeleton.markers[14].pose.orientation.y,skeleton.markers[14].pose.orientation.z,skeleton.markers[14].pose.orientation.w,skeleton.markers[14].id,label])   
                            writer.writerow([skeleton.markers[15].pose.orientation.x,skeleton.markers[15].pose.orientation.y,skeleton.markers[15].pose.orientation.z,skeleton.markers[15].pose.orientation.w,skeleton.markers[15].id,label])   
                            writer.writerow([skeleton.markers[16].pose.orientation.x,skeleton.markers[16].pose.orientation.y,skeleton.markers[16].pose.orientation.z,skeleton.markers[16].pose.orientation.w,skeleton.markers[16].id,label])   
                            writer.writerow([skeleton.markers[17].pose.orientation.x,skeleton.markers[17].pose.orientation.y,skeleton.markers[17].pose.orientation.z,skeleton.markers[17].pose.orientation.w,skeleton.markers[17].id,label])   
                            writer.writerow([skeleton.markers[18].pose.orientation.x,skeleton.markers[18].pose.orientation.y,skeleton.markers[18].pose.orientation.z,skeleton.markers[18].pose.orientation.w,skeleton.markers[18].id,label])   
                            writer.writerow([skeleton.markers[19].pose.orientation.x,skeleton.markers[19].pose.orientation.y,skeleton.markers[19].pose.orientation.z,skeleton.markers[19].pose.orientation.w,skeleton.markers[19].id,label])   
                            writer.writerow([skeleton.markers[20].pose.orientation.x,skeleton.markers[20].pose.orientation.y,skeleton.markers[20].pose.orientation.z,skeleton.markers[20].pose.orientation.w,skeleton.markers[20].id,label])   
                            writer.writerow([skeleton.markers[21].pose.orientation.x,skeleton.markers[21].pose.orientation.y,skeleton.markers[21].pose.orientation.z,skeleton.markers[21].pose.orientation.w,skeleton.markers[21].id,label])   
                            writer.writerow([skeleton.markers[22].pose.orientation.x,skeleton.markers[22].pose.orientation.y,skeleton.markers[22].pose.orientation.z,skeleton.markers[22].pose.orientation.w,skeleton.markers[22].id,label])   
                            writer.writerow([skeleton.markers[23].pose.orientation.x,skeleton.markers[23].pose.orientation.y,skeleton.markers[23].pose.orientation.z,skeleton.markers[23].pose.orientation.w,skeleton.markers[23].id,label])   
                            writer.writerow([skeleton.markers[24].pose.orientation.x,skeleton.markers[24].pose.orientation.y,skeleton.markers[24].pose.orientation.z,skeleton.markers[24].pose.orientation.w,skeleton.markers[24].id,label])   
                            writer.writerow([skeleton.markers[25].pose.orientation.x,skeleton.markers[25].pose.orientation.y,skeleton.markers[25].pose.orientation.z,skeleton.markers[25].pose.orientation.w,skeleton.markers[25].id,label])   
                            writer.writerow([skeleton.markers[26].pose.orientation.x,skeleton.markers[26].pose.orientation.y,skeleton.markers[26].pose.orientation.z,skeleton.markers[26].pose.orientation.w,skeleton.markers[26].id,label])   
                            writer.writerow([skeleton.markers[27].pose.orientation.x,skeleton.markers[27].pose.orientation.y,skeleton.markers[27].pose.orientation.z,skeleton.markers[27].pose.orientation.w,skeleton.markers[27].id,label])   
                            writer.writerow([skeleton.markers[28].pose.orientation.x,skeleton.markers[28].pose.orientation.y,skeleton.markers[28].pose.orientation.z,skeleton.markers[28].pose.orientation.w,skeleton.markers[28].id,label])   
                            writer.writerow([skeleton.markers[29].pose.orientation.x,skeleton.markers[29].pose.orientation.y,skeleton.markers[29].pose.orientation.z,skeleton.markers[29].pose.orientation.w,skeleton.markers[29].id,label])   
                            writer.writerow([skeleton.markers[30].pose.orientation.x,skeleton.markers[30].pose.orientation.y,skeleton.markers[30].pose.orientation.z,skeleton.markers[30].pose.orientation.w,skeleton.markers[30].id,label])   
                            writer.writerow([skeleton.markers[31].pose.orientation.x,skeleton.markers[31].pose.orientation.y,skeleton.markers[31].pose.orientation.z,skeleton.markers[31].pose.orientation.w,skeleton.markers[31].id,label])   
                        else:
                            writer.writerow([skeleton.markers[0].pose.position.x,skeleton.markers[0].pose.position.y,skeleton.markers[0].pose.position.z,skeleton.markers[0].id,label])   
                            writer.writerow([skeleton.markers[1].pose.position.x,skeleton.markers[1].pose.position.y,skeleton.markers[1].pose.position.z,skeleton.markers[1].id,label])   
                            writer.writerow([skeleton.markers[2].pose.position.x,skeleton.markers[2].pose.position.y,skeleton.markers[2].pose.position.z,skeleton.markers[2].id,label])   
                            writer.writerow([skeleton.markers[3].pose.position.x,skeleton.markers[3].pose.position.y,skeleton.markers[3].pose.position.z,skeleton.markers[3].id,label])   
                            writer.writerow([skeleton.markers[4].pose.position.x,skeleton.markers[4].pose.position.y,skeleton.markers[4].pose.position.z,skeleton.markers[4].id,label])   
                            writer.writerow([skeleton.markers[5].pose.position.x,skeleton.markers[5].pose.position.y,skeleton.markers[5].pose.position.z,skeleton.markers[5].id,label])   
                            writer.writerow([skeleton.markers[6].pose.position.x,skeleton.markers[6].pose.position.y,skeleton.markers[6].pose.position.z,skeleton.markers[6].id,label])   
                            writer.writerow([skeleton.markers[7].pose.position.x,skeleton.markers[7].pose.position.y,skeleton.markers[7].pose.position.z,skeleton.markers[7].id,label])   
                            writer.writerow([skeleton.markers[8].pose.position.x,skeleton.markers[8].pose.position.y,skeleton.markers[8].pose.position.z,skeleton.markers[8].id,label])   
                            writer.writerow([skeleton.markers[9].pose.position.x,skeleton.markers[9].pose.position.y,skeleton.markers[9].pose.position.z,skeleton.markers[9].id,label])   
                            writer.writerow([skeleton.markers[10].pose.position.x,skeleton.markers[10].pose.position.y,skeleton.markers[10].pose.position.z,skeleton.markers[10].id,label])   
                            writer.writerow([skeleton.markers[11].pose.position.x,skeleton.markers[11].pose.position.y,skeleton.markers[11].pose.position.z,skeleton.markers[11].id,label])   
                            writer.writerow([skeleton.markers[12].pose.position.x,skeleton.markers[12].pose.position.y,skeleton.markers[12].pose.position.z,skeleton.markers[12].id,label])   
                            writer.writerow([skeleton.markers[13].pose.position.x,skeleton.markers[13].pose.position.y,skeleton.markers[13].pose.position.z,skeleton.markers[13].id,label])   
                            writer.writerow([skeleton.markers[14].pose.position.x,skeleton.markers[14].pose.position.y,skeleton.markers[14].pose.position.z,skeleton.markers[14].id,label])   
                            writer.writerow([skeleton.markers[15].pose.position.x,skeleton.markers[15].pose.position.y,skeleton.markers[15].pose.position.z,skeleton.markers[15].id,label])   
                            writer.writerow([skeleton.markers[16].pose.position.x,skeleton.markers[16].pose.position.y,skeleton.markers[16].pose.position.z,skeleton.markers[16].id,label])   
                            writer.writerow([skeleton.markers[17].pose.position.x,skeleton.markers[17].pose.position.y,skeleton.markers[17].pose.position.z,skeleton.markers[17].id,label])   
                            writer.writerow([skeleton.markers[18].pose.position.x,skeleton.markers[18].pose.position.y,skeleton.markers[18].pose.position.z,skeleton.markers[18].id,label])   
                            writer.writerow([skeleton.markers[19].pose.position.x,skeleton.markers[19].pose.position.y,skeleton.markers[19].pose.position.z,skeleton.markers[19].id,label])   
                            writer.writerow([skeleton.markers[20].pose.position.x,skeleton.markers[20].pose.position.y,skeleton.markers[20].pose.position.z,skeleton.markers[20].id,label])   
                            writer.writerow([skeleton.markers[21].pose.position.x,skeleton.markers[21].pose.position.y,skeleton.markers[21].pose.position.z,skeleton.markers[21].id,label])   
                            writer.writerow([skeleton.markers[22].pose.position.x,skeleton.markers[22].pose.position.y,skeleton.markers[22].pose.position.z,skeleton.markers[22].id,label])   
                            writer.writerow([skeleton.markers[23].pose.position.x,skeleton.markers[23].pose.position.y,skeleton.markers[23].pose.position.z,skeleton.markers[23].id,label])   
                            writer.writerow([skeleton.markers[24].pose.position.x,skeleton.markers[24].pose.position.y,skeleton.markers[24].pose.position.z,skeleton.markers[24].id,label])   
                            writer.writerow([skeleton.markers[25].pose.position.x,skeleton.markers[25].pose.position.y,skeleton.markers[25].pose.position.z,skeleton.markers[25].id,label])   
                            writer.writerow([skeleton.markers[26].pose.position.x,skeleton.markers[26].pose.position.y,skeleton.markers[26].pose.position.z,skeleton.markers[26].id,label])   
                            writer.writerow([skeleton.markers[27].pose.position.x,skeleton.markers[27].pose.position.y,skeleton.markers[27].pose.position.z,skeleton.markers[27].id,label])   
                            writer.writerow([skeleton.markers[28].pose.position.x,skeleton.markers[28].pose.position.y,skeleton.markers[28].pose.position.z,skeleton.markers[28].id,label])   
                            writer.writerow([skeleton.markers[29].pose.position.x,skeleton.markers[29].pose.position.y,skeleton.markers[29].pose.position.z,skeleton.markers[29].id,label])   
                            writer.writerow([skeleton.markers[30].pose.position.x,skeleton.markers[30].pose.position.y,skeleton.markers[30].pose.position.z,skeleton.markers[30].id,label])   
                            writer.writerow([skeleton.markers[31].pose.position.x,skeleton.markers[31].pose.position.y,skeleton.markers[31].pose.position.z,skeleton.markers[31].id,label])   
                            #p_des_1 = [skeletons.markers[i].pose.position.z for i in range(len(skeletons.markers))]
                    except:
                        print(j," missing")
                    #t_des = [skeletons.pose[i].time_from_start.sec + trajectory.points[i].time_from_start.nanosec*1e-9 for i in range(len(trajectory.points))]
                    #p_des_1 = [trajectory.points[i].positions[0] for i in range(len(trajectory.points))]
                    #t_des = [trajectory.points[i].time_from_start.sec + trajectory.points[i].time_from_start.nanosec*1e-9 for i in range(len(trajectory.points))]

                    #actual = parser.get_messages("/joint_states")

                    #plt.plot(p_des_1)

                    #plt.show()
