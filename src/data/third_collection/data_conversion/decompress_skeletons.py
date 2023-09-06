import zstandard
import pathlib

tags = ['s1_s2_r1_p1_s1_','s1_s2_r1_p1_s2_','s1_s2_r1_p2_s1_','s1_s2_r1_p2_s2_',
        's1_s2_r2_p1_s1_','s1_s2_r2_p1_s2_','s1_s2_r2_p2_s1_','s1_s2_r2_p2_s2_',
        's1_s3_r1_p1_s1_','s1_s3_r1_p1_s2_','s1_s3_r1_p2_s1_','s1_s3_r1_p2_s2_',
        's1_s3_r2_p1_s1_','s1_s3_r2_p1_s2_','s1_s3_r2_p2_s1_','s1_s3_r2_p2_s2_',
        's3_s2_r1_p1_s1_','s3_s2_r1_p1_s2_','s3_s2_r1_p2_s1_','s3_s2_r1_p2_s2_',
        's3_s2_r2_p1_s1_','s3_s2_r2_p1_s2_','s3_s2_r2_p2_s1_','s3_s2_r2_p2_s2_']
        
data_type = ['skeleton','label']

for i in data_type:
    for j in tags:
        input_file = "/media/francesco/Corolab/test_recording_original/"+"test_pairs_"+j+i+"/test_pairs_"+j+i+"_0.db3.zst"
        try:
            with open(input_file, 'rb') as compressed:
                decomp = zstandard.ZstdDecompressor()
                output_path = "src/data/third_collection/db3/test_pairs_"+j+i+".db3"
                with open(output_path, 'wb') as destination:
                    decomp.copy_stream(compressed, destination)
        except:
            print(input_file," missing")