# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
import pandas as pd
import boto3
from botocore.config import Config

config = Config(
    retries = dict(
        max_attempts = 10
    )
)

ec2 = boto3.client('ec2', config=config)

def detect_labels_local_file(photo,Num_Label):
    client = boto3.client('rekognition')
    labels = [None] * 5
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    # print('Detected labels in ' + photo)
    i = 0
    for label in response['Labels']:
        if i == 5:
            break
        # print(label['Name'] + ' : ' + str(label['Confidence']))
        labels[i] = label['Name']
        i = i + 1
    # for i in range(Num_Label):
    #     label = response['Labels'][i]
    #     # print(label['Name'])
    #     labels.append(label['Name'])
    # return len(response['Labels'])
    return labels

def write_Result_csv(data_folder,reading_address,writing_address):
    num_label = 5
    dataset = pd.read_csv(reading_address)
    data_size = dataset.shape[0]
    df = pd.DataFrame(columns=['imageID', '1', '2', '3', '4', '5'])
    # data_address = data_folder + str(dataset.iloc[2, 0]).zfill(5) + '.jpg'
    # labels = detect_labels_local_file(data_address, num_label)
    # print(labels)
    # data_size
    for i in range(data_size):
        print(i)
        data_address = data_folder + str(dataset.iloc[i, 0]).zfill(5) + '.jpg'
        labels = detect_labels_local_file(data_address, num_label)
        # print("Labels detected: " + str(label_count))
        labels = [str(dataset.iloc[i, 0]).zfill(5)] + labels
        # print(labels)
        df.loc[len(df)] = labels

    df = df.set_index('imageID')
    df.to_csv(writing_address)

def main():
    write_Result_csv('./test_crop/', 'test_og.csv', 'test_crop_result.csv')
    # write_Result_csv('./train_crop/', 'train.csv', 'train_crop_result.csv')
    # write_Result_csv('./train_grayscale/', 'train.csv', 'train_grayscale_result.csv')
    # write_Result_csv('./train_grayscale_equalization/', 'train.csv', 'train_gyeq_result.csv')
    # write_Result_csv('./test_grayscale/', 'test_og.csv', 'test_grayscale_result.csv')
    # write_Result_csv('./test_grayscale_equalization/', 'test_og.csv', 'test_grayeq_result.csv')
    # write_Result_csv('./test_HE/', 'test_og.csv', 'test_HE_result.csv')
    # write_Result_csv('./train_HE/', 'train.csv', 'train_HE_result.csv')
    # write_Result_csv('./test_bila/', 'test_og.csv', 'test_bila_result.csv')
    # write_Result_csv('./train_bila/', 'train.csv', 'train_bila_result.csv')
    # write_Result_csv('./test_laplacian/', 'test_og.csv', 'test_lap_result.csv')
    # write_Result_csv('./train_laplacian/', 'train.csv', 'train_lap_result.csv')
    # write_Result_csv('./test_midpoint/', 'test_og.csv', 'test_mid_result.csv')
    # write_Result_csv('./train_midpoint/', 'train.csv', 'train_mid_result.csv')

if __name__ == "__main__":
    main()