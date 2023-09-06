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

    #subjects = ['s01','s02','s03','s04','s05','s06','s07','s08','s09','s10','s11']
    #subjects = ['s10','s11']
    subjects = ['s02','s05']

    '''tags = ['_a01_t01_r01','_a01_t01_r02','_a01_t01_r03','_a01_t01_r04','_a01_t01_r05','_a01_t01_r06',
    '_a01_t02_r01','_a01_t02_r02','_a01_t02_r03','_a01_t02_r04','_a01_t02_r05','_a01_t02_r06',
    '_a01_t03_r01','_a01_t03_r02','_a01_t03_r03','_a01_t03_r04','_a01_t03_r05','_a01_t03_r06',
    '_a01_t04_r01','_a01_t04_r02','_a01_t04_r03','_a01_t04_r04','_a01_t04_r05','_a01_t04_r06',
    '_a01_t05_r01','_a01_t05_r02','_a01_t05_r03','_a01_t05_r04','_a01_t05_r05','_a01_t05_r06',
    '_a02_t01_r01','_a02_t01_r02','_a02_t01_r03','_a02_t01_r04','_a02_t01_r05','_a02_t01_r06',
    '_a02_t02_r01','_a02_t02_r02','_a02_t02_r03','_a02_t02_r04','_a02_t02_r05','_a02_t02_r06',
    '_a02_t03_r01','_a02_t03_r02','_a02_t03_r03','_a02_t03_r04','_a02_t03_r05','_a02_t03_r06',
    '_a02_t04_r01','_a02_t04_r02','_a02_t04_r03','_a02_t04_r04','_a02_t04_r05','_a02_t04_r06',
    '_a02_t05_r01','_a02_t05_r02','_a02_t05_r03','_a02_t05_r04','_a02_t05_r05','_a02_t05_r06',
    '_a03_t01_r01','_a03_t01_r02','_a03_t01_r03','_a03_t01_r04','_a03_t01_r05','_a03_t01_r06',
    '_a03_t02_r01','_a03_t02_r02','_a03_t02_r03','_a03_t02_r04','_a03_t02_r05','_a03_t02_r06',
    '_a03_t03_r01','_a03_t03_r02','_a03_t03_r03','_a03_t03_r04','_a03_t03_r05','_a03_t03_r06',
    '_a03_t04_r01','_a03_t04_r02','_a03_t04_r03','_a03_t04_r04','_a03_t04_r05','_a03_t04_r06',
    '_a03_t05_r01','_a03_t05_r02','_a03_t05_r03','_a03_t05_r04','_a03_t05_r05','_a03_t05_r06']
'''

    tags = ['_a01_t01_r01','_a01_t01_r06',
        '_a01_t02_r01','_a01_t02_r06',
        '_a01_t03_r01','_a01_t03_r06',
        '_a01_t04_r01','_a01_t04_r06',
        '_a01_t05_r01','_a01_t05_r06',
        '_a02_t01_r01','_a02_t01_r06',
        '_a02_t02_r01','_a02_t02_r06',
        '_a02_t03_r01','_a02_t03_r06',
        '_a02_t04_r01','_a02_t04_r06',
        '_a02_t05_r01','_a02_t05_r06',
        '_a03_t01_r01','_a03_t01_r06',
        '_a03_t02_r01','_a03_t02_r06',
        '_a03_t03_r01','_a03_t03_r06',
        '_a03_t04_r01','_a03_t04_r06',
        '_a03_t05_r01','_a03_t05_r06']

    preprocess_data = False

    full_tags = []

    for i in subjects:

        for j in tags:

            full_tags.append(i+j)

    for i in full_tags:

        if i =='s10_a01_t04_r01':
            continue
        print(i)
        parser = BagFileParser("../db3/" + i + '_skeleton_0.db3')

        if preprocess_data:
            new_file = "../prep/" + i + '_prep.csv'
        else:
            new_file = "../csv/" + i + '.csv'

        with open(new_file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            for k in (range(len(parser.get_messages("body_tracking_data")))):
            
                skeleton = parser.get_messages("body_tracking_data")[k][1] 
                
                try:
                    # write the header
                    if preprocess_data:
                        writer.writerow([skeleton.markers[0].pose.orientation.x,skeleton.markers[0].pose.orientation.y,skeleton.markers[0].pose.orientation.z,skeleton.markers[0].pose.orientation.w])   
                        writer.writerow([skeleton.markers[1].pose.orientation.x,skeleton.markers[1].pose.orientation.y,skeleton.markers[1].pose.orientation.z,skeleton.markers[1].pose.orientation.w])   
                        writer.writerow([skeleton.markers[2].pose.orientation.x,skeleton.markers[2].pose.orientation.y,skeleton.markers[2].pose.orientation.z,skeleton.markers[2].pose.orientation.w])   
                        writer.writerow([skeleton.markers[3].pose.orientation.x,skeleton.markers[3].pose.orientation.y,skeleton.markers[3].pose.orientation.z,skeleton.markers[3].pose.orientation.w])   
                        writer.writerow([skeleton.markers[4].pose.orientation.x,skeleton.markers[4].pose.orientation.y,skeleton.markers[4].pose.orientation.z,skeleton.markers[4].pose.orientation.w])   
                        writer.writerow([skeleton.markers[5].pose.orientation.x,skeleton.markers[5].pose.orientation.y,skeleton.markers[5].pose.orientation.z,skeleton.markers[5].pose.orientation.w])   
                        writer.writerow([skeleton.markers[6].pose.orientation.x,skeleton.markers[6].pose.orientation.y,skeleton.markers[6].pose.orientation.z,skeleton.markers[6].pose.orientation.w])   
                        writer.writerow([skeleton.markers[7].pose.orientation.x,skeleton.markers[7].pose.orientation.y,skeleton.markers[7].pose.orientation.z,skeleton.markers[7].pose.orientation.w])   
                        writer.writerow([skeleton.markers[8].pose.orientation.x,skeleton.markers[8].pose.orientation.y,skeleton.markers[8].pose.orientation.z,skeleton.markers[8].pose.orientation.w])   
                        writer.writerow([skeleton.markers[9].pose.orientation.x,skeleton.markers[9].pose.orientation.y,skeleton.markers[9].pose.orientation.z,skeleton.markers[9].pose.orientation.w])   
                        writer.writerow([skeleton.markers[10].pose.orientation.x,skeleton.markers[10].pose.orientation.y,skeleton.markers[10].pose.orientation.z,skeleton.markers[10].pose.orientation.w])   
                        writer.writerow([skeleton.markers[11].pose.orientation.x,skeleton.markers[11].pose.orientation.y,skeleton.markers[11].pose.orientation.z,skeleton.markers[11].pose.orientation.w])   
                        writer.writerow([skeleton.markers[12].pose.orientation.x,skeleton.markers[12].pose.orientation.y,skeleton.markers[12].pose.orientation.z,skeleton.markers[12].pose.orientation.w])   
                        writer.writerow([skeleton.markers[13].pose.orientation.x,skeleton.markers[13].pose.orientation.y,skeleton.markers[13].pose.orientation.z,skeleton.markers[13].pose.orientation.w])   
                        writer.writerow([skeleton.markers[14].pose.orientation.x,skeleton.markers[14].pose.orientation.y,skeleton.markers[14].pose.orientation.z,skeleton.markers[14].pose.orientation.w])   
                        writer.writerow([skeleton.markers[15].pose.orientation.x,skeleton.markers[15].pose.orientation.y,skeleton.markers[15].pose.orientation.z,skeleton.markers[15].pose.orientation.w])   
                        writer.writerow([skeleton.markers[16].pose.orientation.x,skeleton.markers[16].pose.orientation.y,skeleton.markers[16].pose.orientation.z,skeleton.markers[16].pose.orientation.w])   
                        writer.writerow([skeleton.markers[17].pose.orientation.x,skeleton.markers[17].pose.orientation.y,skeleton.markers[17].pose.orientation.z,skeleton.markers[17].pose.orientation.w])   
                        writer.writerow([skeleton.markers[18].pose.orientation.x,skeleton.markers[18].pose.orientation.y,skeleton.markers[18].pose.orientation.z,skeleton.markers[18].pose.orientation.w])   
                        writer.writerow([skeleton.markers[19].pose.orientation.x,skeleton.markers[19].pose.orientation.y,skeleton.markers[19].pose.orientation.z,skeleton.markers[19].pose.orientation.w])   
                        writer.writerow([skeleton.markers[20].pose.orientation.x,skeleton.markers[20].pose.orientation.y,skeleton.markers[20].pose.orientation.z,skeleton.markers[20].pose.orientation.w])   
                        writer.writerow([skeleton.markers[21].pose.orientation.x,skeleton.markers[21].pose.orientation.y,skeleton.markers[21].pose.orientation.z,skeleton.markers[21].pose.orientation.w])   
                        writer.writerow([skeleton.markers[22].pose.orientation.x,skeleton.markers[22].pose.orientation.y,skeleton.markers[22].pose.orientation.z,skeleton.markers[22].pose.orientation.w])   
                        writer.writerow([skeleton.markers[23].pose.orientation.x,skeleton.markers[23].pose.orientation.y,skeleton.markers[23].pose.orientation.z,skeleton.markers[23].pose.orientation.w])   
                        writer.writerow([skeleton.markers[24].pose.orientation.x,skeleton.markers[24].pose.orientation.y,skeleton.markers[24].pose.orientation.z,skeleton.markers[24].pose.orientation.w])   
                        writer.writerow([skeleton.markers[25].pose.orientation.x,skeleton.markers[25].pose.orientation.y,skeleton.markers[25].pose.orientation.z,skeleton.markers[25].pose.orientation.w])   
                        writer.writerow([skeleton.markers[26].pose.orientation.x,skeleton.markers[26].pose.orientation.y,skeleton.markers[26].pose.orientation.z,skeleton.markers[26].pose.orientation.w])   
                        writer.writerow([skeleton.markers[27].pose.orientation.x,skeleton.markers[27].pose.orientation.y,skeleton.markers[27].pose.orientation.z,skeleton.markers[27].pose.orientation.w])   
                        writer.writerow([skeleton.markers[28].pose.orientation.x,skeleton.markers[28].pose.orientation.y,skeleton.markers[28].pose.orientation.z,skeleton.markers[28].pose.orientation.w])   
                        writer.writerow([skeleton.markers[29].pose.orientation.x,skeleton.markers[29].pose.orientation.y,skeleton.markers[29].pose.orientation.z,skeleton.markers[29].pose.orientation.w])   
                        writer.writerow([skeleton.markers[30].pose.orientation.x,skeleton.markers[30].pose.orientation.y,skeleton.markers[30].pose.orientation.z,skeleton.markers[30].pose.orientation.w])   
                        writer.writerow([skeleton.markers[31].pose.orientation.x,skeleton.markers[31].pose.orientation.y,skeleton.markers[31].pose.orientation.z,skeleton.markers[31].pose.orientation.w])   
                    else:
                        writer.writerow([skeleton.markers[0].pose.position.x,skeleton.markers[0].pose.position.y,skeleton.markers[0].pose.position.z])   
                        writer.writerow([skeleton.markers[1].pose.position.x,skeleton.markers[1].pose.position.y,skeleton.markers[1].pose.position.z])   
                        writer.writerow([skeleton.markers[2].pose.position.x,skeleton.markers[2].pose.position.y,skeleton.markers[2].pose.position.z])   
                        writer.writerow([skeleton.markers[3].pose.position.x,skeleton.markers[3].pose.position.y,skeleton.markers[3].pose.position.z])   
                        writer.writerow([skeleton.markers[4].pose.position.x,skeleton.markers[4].pose.position.y,skeleton.markers[4].pose.position.z])   
                        writer.writerow([skeleton.markers[5].pose.position.x,skeleton.markers[5].pose.position.y,skeleton.markers[5].pose.position.z])   
                        writer.writerow([skeleton.markers[6].pose.position.x,skeleton.markers[6].pose.position.y,skeleton.markers[6].pose.position.z])   
                        writer.writerow([skeleton.markers[7].pose.position.x,skeleton.markers[7].pose.position.y,skeleton.markers[7].pose.position.z])   
                        writer.writerow([skeleton.markers[8].pose.position.x,skeleton.markers[8].pose.position.y,skeleton.markers[8].pose.position.z])   
                        writer.writerow([skeleton.markers[9].pose.position.x,skeleton.markers[9].pose.position.y,skeleton.markers[9].pose.position.z])   
                        writer.writerow([skeleton.markers[10].pose.position.x,skeleton.markers[10].pose.position.y,skeleton.markers[10].pose.position.z])   
                        writer.writerow([skeleton.markers[11].pose.position.x,skeleton.markers[11].pose.position.y,skeleton.markers[11].pose.position.z])   
                        writer.writerow([skeleton.markers[12].pose.position.x,skeleton.markers[12].pose.position.y,skeleton.markers[12].pose.position.z])   
                        writer.writerow([skeleton.markers[13].pose.position.x,skeleton.markers[13].pose.position.y,skeleton.markers[13].pose.position.z])   
                        writer.writerow([skeleton.markers[14].pose.position.x,skeleton.markers[14].pose.position.y,skeleton.markers[14].pose.position.z])   
                        writer.writerow([skeleton.markers[15].pose.position.x,skeleton.markers[15].pose.position.y,skeleton.markers[15].pose.position.z])   
                        writer.writerow([skeleton.markers[16].pose.position.x,skeleton.markers[16].pose.position.y,skeleton.markers[16].pose.position.z])   
                        writer.writerow([skeleton.markers[17].pose.position.x,skeleton.markers[17].pose.position.y,skeleton.markers[17].pose.position.z])   
                        writer.writerow([skeleton.markers[18].pose.position.x,skeleton.markers[18].pose.position.y,skeleton.markers[18].pose.position.z])   
                        writer.writerow([skeleton.markers[19].pose.position.x,skeleton.markers[19].pose.position.y,skeleton.markers[19].pose.position.z])   
                        writer.writerow([skeleton.markers[20].pose.position.x,skeleton.markers[20].pose.position.y,skeleton.markers[20].pose.position.z])   
                        writer.writerow([skeleton.markers[21].pose.position.x,skeleton.markers[21].pose.position.y,skeleton.markers[21].pose.position.z])   
                        writer.writerow([skeleton.markers[22].pose.position.x,skeleton.markers[22].pose.position.y,skeleton.markers[22].pose.position.z])   
                        writer.writerow([skeleton.markers[23].pose.position.x,skeleton.markers[23].pose.position.y,skeleton.markers[23].pose.position.z])   
                        writer.writerow([skeleton.markers[24].pose.position.x,skeleton.markers[24].pose.position.y,skeleton.markers[24].pose.position.z])   
                        writer.writerow([skeleton.markers[25].pose.position.x,skeleton.markers[25].pose.position.y,skeleton.markers[25].pose.position.z])   
                        writer.writerow([skeleton.markers[26].pose.position.x,skeleton.markers[26].pose.position.y,skeleton.markers[26].pose.position.z])   
                        writer.writerow([skeleton.markers[27].pose.position.x,skeleton.markers[27].pose.position.y,skeleton.markers[27].pose.position.z])   
                        writer.writerow([skeleton.markers[28].pose.position.x,skeleton.markers[28].pose.position.y,skeleton.markers[28].pose.position.z])   
                        writer.writerow([skeleton.markers[29].pose.position.x,skeleton.markers[29].pose.position.y,skeleton.markers[29].pose.position.z])   
                        writer.writerow([skeleton.markers[30].pose.position.x,skeleton.markers[30].pose.position.y,skeleton.markers[30].pose.position.z])   
                        writer.writerow([skeleton.markers[31].pose.position.x,skeleton.markers[31].pose.position.y,skeleton.markers[31].pose.position.z])   
                        #p_des_1 = [skeleton.markers[i].pose.position.z for i in range(len(skeleton.markers))]
                except:
                    print(i," missing")
                #t_des = [skeleton.pose[i].time_from_start.sec + trajectory.points[i].time_from_start.nanosec*1e-9 for i in range(len(trajectory.points))]
                #p_des_1 = [trajectory.points[i].positions[0] for i in range(len(trajectory.points))]
                #t_des = [trajectory.points[i].time_from_start.sec + trajectory.points[i].time_from_start.nanosec*1e-9 for i in range(len(trajectory.points))]

                #actual = parser.get_messages("/joint_states")

                #plt.plot(p_des_1)

                #plt.show()
