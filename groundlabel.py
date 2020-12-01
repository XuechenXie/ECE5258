import boto3
import pandas as pd
import numpy as np

def detect_labels_local_file(photo):
    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('Detected labels in ' + photo)
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

    return len(response['Labels'])

def match_label(labels, useclass):
    for i in range(5):
        is_target_in_list = str(labels[i+1]).lower() in (string.lower() for string in useclass)
        if is_target_in_list:
            return True
    return False

def preproc_df2(reference, challengeType, challengeLevel):
    idx = np.logical_and(reference.challengeLevel == challengeLevel, reference.challengeType == challengeType)
    return idx

def preproc_df1(reference, challengeLevel):
    idx = reference.challengeLevel == challengeLevel
    return idx

def calculate_accuracy(dataset,reference, idx):
    class1 = ['Electronics', 'camera', 'video camera', 'digital camera']
    class2 = ['cone']
    class3 = ['sports', 'sport', 'baseball', 'softball', 'ball', 'sphere']
    class4 = ['frying pan', 'wok']
    class5 = ['toy', 'figurine']
    class6 = ['Electronics', 'cell phone', 'phone', 'mobile phone', 'iphone']
    class7 = ['toothbrush', 'brush', 'tool']
    class8 = ['Electronics', 'Computer', 'Computer Keyboard', 'Computer Hardware', 'Keyboard']
    class9 = ['Bottle', 'Cosmetics']
    class10 = ['Clothing', 'Apparel', 'Shoe', 'Footwear', 'Running Shoe', 'Sneaker']

    correct = 0

    df = dataset.loc[idx]
    ref = reference.loc[idx]

    for i in range(df.shape[0]):
        # id = dataset.iloc[i, 0]
        # print(id)
        class_num = str(ref.iloc[i, 1])
        if class_num == '1':
            useclass = class1
        elif class_num == '2':
            useclass = class2
        elif class_num == '3':
            useclass = class3
        elif class_num == '4':
            useclass = class4
        elif class_num == '5':
            useclass = class5
        elif class_num == '6':
            useclass = class6
        elif class_num == '7':
            useclass = class7
        elif class_num == '8':
            useclass = class8
        elif class_num == '9':
            useclass = class9
        elif class_num == '10':
            useclass = class10
        else:
            useclass = []

        if match_label(df.iloc[i, :], useclass):
            correct = correct + 1

    return correct, df.shape[0]

def write_to_csv(dataset,reference,dataset2,reference2,writing_address):
    df = pd.DataFrame(columns=['Type', 'level', 'correct'])

    challengeType = 1
    challengeLevel = 0

    idx = preproc_df2(reference, challengeType, challengeLevel)
    idx2 = preproc_df2(reference2, challengeType, challengeLevel)
    correct, size = calculate_accuracy(dataset, reference, idx)
    correct2, size2 = calculate_accuracy(dataset2, reference2, idx2)
    # print(challengeType, challengeLevel)
    # print((correct + correct2))

    df.loc[len(df)] = [challengeType,challengeLevel,(correct + correct2)]

    challengeType = 10
    challengeLevel = 0

    idx = preproc_df2(reference, challengeType, challengeLevel)
    idx2 = preproc_df2(reference2, challengeType, challengeLevel)
    correct, size = calculate_accuracy(dataset, reference, idx)
    correct2, size2 = calculate_accuracy(dataset2, reference2, idx2)
    # print(challengeType, challengeLevel)
    # print((correct + correct2))
    df.loc[len(df)] = [challengeType, challengeLevel, (correct + correct2)]

    challengeType = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]
    challengeLevel = [1, 2, 3, 4]

    for i in range(16):
        for j in range(4):
            idx = preproc_df2(reference, challengeType[i], challengeLevel[j])
            idx2 = preproc_df2(reference2, challengeType[i], challengeLevel[j])
            correct, size = calculate_accuracy(dataset, reference, idx)
            correct2, size2 = calculate_accuracy(dataset2, reference2, idx2)
            # print(challengeType[i], challengeLevel[j])
            # print((correct + correct2))
            df.loc[len(df)] = [challengeType[i], challengeLevel[j], (correct + correct2)]

    df.to_csv(writing_address)


def main():
    dataset = pd.read_csv('test_bila_result.csv')
    reference = pd.read_csv('test_og.csv')

    dataset2 = pd.read_csv('train_bila_result.csv')
    reference2 = pd.read_csv('train.csv')

    writing_address = 'Bilateral_accuracy_result.csv'


    write_to_csv(dataset,reference,dataset2,reference2,writing_address)
    # challengeType = 1
    # challengeLevel = 0
    #
    # idx = preproc_df2(reference, challengeType, challengeLevel)
    # idx2 = preproc_df2(reference2, challengeType, challengeLevel)
    # correct, size = calculate_accuracy(dataset, reference, idx)
    # correct2, size2 = calculate_accuracy(dataset2, reference2, idx2)
    # print(challengeType, challengeLevel)
    # print((correct + correct2))
    #
    # challengeType = 10
    # challengeLevel = 0
    #
    # idx = preproc_df2(reference, challengeType, challengeLevel)
    # idx2 = preproc_df2(reference2, challengeType, challengeLevel)
    # correct, size = calculate_accuracy(dataset, reference, idx)
    # correct2, size2 = calculate_accuracy(dataset2, reference2, idx2)
    # print(challengeType, challengeLevel)
    # print((correct + correct2))
    #
    # challengeType = [2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18]
    # challengeLevel = [1,2,3,4]
    #
    # for i in range(16):
    #     for j in range(4):
    #         idx = preproc_df2(reference, challengeType[i], challengeLevel[j])
    #         idx2 = preproc_df2(reference2, challengeType[i], challengeLevel[j])
    #         correct, size = calculate_accuracy(dataset, reference, idx)
    #         correct2, size2 = calculate_accuracy(dataset2, reference2, idx2)
    #         print(challengeType[i],challengeLevel[j])
    #         print((correct + correct2))


    # idx = preproc_df2(reference, challengeType, challengeLevel)
    # idx2 = preproc_df2(reference2, challengeType, challengeLevel)
    # idx = preproc_df1(reference, challengeLevel)
    # A = reference.challengeLevel == challengeLevel
    # print(A)
    # print(A.shape)
    # print(idx)




if __name__ == "__main__":
    main()
