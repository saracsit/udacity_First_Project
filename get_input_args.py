import argparse
def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default = 'pet_images/', help = 'path to the folder of pet images')
    parser.add_argument('--arch', type=str, default ='resnet',help=' algorithm used to test classification')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',help ='file of dog names')
    in_args = parser.parse_args()
    return in_args
