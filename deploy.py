import os
import csv
import numpy as np

# Dataset
DATASET = 'pratheepan'

# Determine which variation of the skin detector binary is being used:
#   1. cbs - the original rule by Nadia Brancati
#   2. crs - the reversed rule based on Cr component
#   3. cmb - #1 and #2 rules combined
#   4. ngh - the combined rule with neighborhood approach
SKIN_DETECTOR_VAR = 'cbs'

GT_DATABASE_PATH = DATASET +'/GT/'
GTC_DATABASE_PATH = DATASET +'/GT_COLOR/'
PREDICTED_DATABASE_PATH = DATASET +\
                        '/PREDICTED/'+ SKIN_DETECTOR_VAR + '/'
ORI_DATABASE_PATH = DATASET +'/ORI/'
# path for the trapezia generated from the method
PREDICTED_TRAPEZIA_PATH = PREDICTED_DATABASE_PATH + 'trapezia/'


def reset_global_variables():
    global GT_DATABASE_PATH, PREDICTED_DATABASE_PATH, \
            ORI_DATABASE_PATH, PREDICTED_TRAPEZIA_PATH

    GT_DATABASE_PATH = DATASET +'/GT/'
    GTC_DATABASE_PATH = DATASET +'/GT_COLOR/'
    PREDICTED_DATABASE_PATH = DATASET +\
                            '/PREDICTED/'+ SKIN_DETECTOR_VAR + '/'
    ORI_DATABASE_PATH = DATASET +'/ORI/'

    PREDICTED_TRAPEZIA_PATH = PREDICTED_DATABASE_PATH + 'trapezia/'


def main():
    global DATASET
    global SKIN_DETECTOR_VAR

    for d in ['pratheepan', 'sfa', 'hgr']:
        for v in ['cbs', 'crs', 'cmb', 'ngh']:
            DATASET = d
            SKIN_DETECTOR_VAR = v

            print('Deploying '+ DATASET + ' dataset with '+ SKIN_DETECTOR_VAR)
            print(80*'=')
            reset_global_variables()

            csv_path = PREDICTED_DATABASE_PATH + DATASET + '_metrics.csv'
            # ignore first and last rows
            csv_data = np.genfromtxt(csv_path, delimiter=',', dtype=str)[1:-1,:]
            for row in csv_data:
                file, precision, recall, specificity, fmeasure = str(row[0]), \
                                            row[1], row[2], row[3], row[4]

                ori_ext = '.jpg'
                gt_ext = '.bmp' if DATASET == 'hgr' else '.png'
                gtc_ext = '.jpg'
                file = file[0:file.rfind('.')]

                command = "python ../manage.py populate_db"
                command += " --ori "+ ORI_DATABASE_PATH + file + ori_ext
                command += " --gtc "+ GTC_DATABASE_PATH + file + gtc_ext
                command += " --gt  "+ GT_DATABASE_PATH + file + gt_ext
                command += " --out "+ PREDICTED_DATABASE_PATH + file + ".bmp "
                command += " --tra "+ PREDICTED_TRAPEZIA_PATH + file + ".jpg "
                command += " --pr "+ precision
                command += " --re "+ recall
                command += " --sp "+ specificity
                command += " --fm "+ fmeasure
                command += " --dataset_id 1"
                os.system(command)

if __name__ == "__main__":
    main()