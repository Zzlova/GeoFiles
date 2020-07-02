import os


def main():
    fold_n = "2020-04-24T11-33-38_5"
    file_n = 'bas_sol.64f'
    bas_sol = {}
    lf = list_files(fold_n)
    num = len(lf)
    print("Количество файлов: ", num)
    for i in range(0, num):
        print(os.path.splitext(lf[i])[1])

    with open(fold_n + "/" + file_n) as file_object:
        contents = file_object.read()
    print(contents)

    bas_sol['Year'] = contents[0:4]
    bas_sol['Month'] = contents[4:6]
    bas_sol['Day'] = contents[6:8]
    bas_sol['Hour'] = contents[8:10]
    bas_sol['Minute'] = contents[10:12]
    bas_sol['Second'] = contents[12:14] + "." + contents[14:16]
    bas_sol['Latitude'] = contents[16:19] + "." + contents[19:23]
    bas_sol['Longitude'] = contents[23:27] + "." + contents[27:31]
    bas_sol['Depth'] = contents[31:34] + "." + contents[34:36]
    bas_sol['M_max'] = contents[36:37] + "." + contents[37:39]
    bas_sol['mb'] = contents[39:40] + "." + contents[40:42]
    bas_sol['Ms'] = contents[42:43] + "." + contents[43:45]
    bas_sol['DHypo'] = contents[45:46]
    bas_sol['Source'] = contents[46:51]
    bas_sol['ID'] = contents[55:65]

    n = contents.find("_Kf", 66)
    if n != -1:
        bas_sol['_Kf'] = contents[n + 3:n + 5] + "." + contents[n + 5:n + 6]

    n = contents.find("_sol", 66)
    if n != -1:
        bas_sol['_sol_1'] = contents[n + 4:n + 8]
        bas_sol['_sol_2'] = contents[n + 8:n + 9] + "." + contents[n + 9:n + 12]

    n = contents.find("_qbt", 66)
    if n != -1:
        bas_sol['_qbt'] = contents[n + 4:n + 5] + "." + contents[n + 5:n + 7]

    n = contents.find("_qfu", 66)
    if n != -1:
        bas_sol['_qfu_1'] = contents[n + 4:n + 5] + "." + contents[n + 5:n + 7]
        bas_sol['_qfu_2'] = contents[n + 7:n + 8] + "." + contents[n + 8:n + 10]

    n = contents.find("_tv", 66)
    if n != -1:
        bas_sol['_tv_1'] = contents[n + 3:n + 16]
        bas_sol['_tv_2'] = contents[n + 16:n + 29]
        bas_sol['_tv_3'] = contents[n + 29:n + 42]
        bas_sol['_tv_4'] = contents[n + 42:n + 55]
        bas_sol['_tv_5'] = contents[n + 55:n + 68]

    n = contents.find("_cTv", 66)
    if n != -1:
        bas_sol['_cTv_1'] = contents[n + 4:n + 7] + "."
        bas_sol['_cTv_2'] = contents[n + 7:n + 10]

    n = contents.find("_eTv", 66)
    if n != -1:
        bas_sol['_eTv_1'] = contents[n + 4:n + 7] + "."
        bas_sol['_eTv_2'] = contents[n + 7:n + 10]

    n = contents.find("_dc", 66)
    if n != -1:
        bas_sol['_dc_11'] = contents[n + 3:n + 7] + "." + contents[n + 7:n + 8]
        bas_sol['_dc_12'] = contents[n + 8:n + 11] + "." + contents[n + 11:n + 12]
        bas_sol['_dc_13'] = contents[n + 12:n + 16] + "." + contents[n + 16:n + 17]
        bas_sol['_dc_21'] = contents[n + 17:n + 21] + "." + contents[n + 21:n + 22]
        bas_sol['_dc_22'] = contents[n + 22:n + 25] + "." + contents[n + 25:n + 26]
        bas_sol['_dc_23'] = contents[n + 26:n + 30] + "." + contents[n + 30:n + 31]

    n = contents.find("_cDC", 66)
    if n != -1:
        bas_sol['_cDC_1'] = contents[n + 4:n + 7] + "."
        bas_sol['_cDC_2'] = contents[n + 7:n + 10]

    n = contents.find("_eDC", 66)
    if n != -1:
        bas_sol['_eDC_1'] = contents[n + 4:n + 7] + "."
        bas_sol['_eDC_2'] = contents[n + 7:n + 10]

    n = contents.find("_cdc", 66)
    if n != -1:
        bas_sol['_cdc_11'] = contents[n + 4:n + 6] + "."
        bas_sol['_cdc_12'] = contents[n + 6:n + 9] + "."
        bas_sol['_cdc_21'] = contents[n + 9:n + 11] + "."
        bas_sol['_cdc_22'] = contents[n + 11:n + 14] + "."

    n = contents.find("_edc", 66)
    if n != -1:
        bas_sol['_edc_11'] = contents[n + 4:n + 6] + "."
        bas_sol['_edc_12'] = contents[n + 6:n + 9] + "."
        bas_sol['_edc_21'] = contents[n + 9:n + 11] + "."
        bas_sol['_edc_22'] = contents[n + 11:n + 14] + "."

    n = contents.find("_TNP", 66)
    if n != -1:
        bas_sol['_TNP_11'] = contents[n + 4:n + 8] + "." + contents[n + 8:n + 9]
        bas_sol['_TNP_12'] = contents[n + 9:n + 12] + "." + contents[n + 12:n + 13]
        bas_sol['_TNP_21'] = contents[n + 13:n + 17] + "." + contents[n + 17:n + 18]
        bas_sol['_TNP_22'] = contents[n + 18:n + 21] + "." + contents[n + 21:n + 22]
        bas_sol['_TNP_31'] = contents[n + 22:n + 26] + "." + contents[n + 26:n + 27]
        bas_sol['_TNP_32'] = contents[n + 27:n + 30] + "." + contents[n + 30:n + 31]

    n = contents.find("_cTNP", 66)
    if n != -1:
        bas_sol['_cTNP_1'] = contents[n + 5:n + 7] + "."
        bas_sol['_cTNP_2'] = contents[n + 7:n + 9] + "."
        bas_sol['_cTNP_3'] = contents[n + 9:n + 11] + "."

    n = contents.find("_eTNP", 66)
    if n != -1:
        bas_sol['_eTNP_1'] = contents[n + 5:n + 7] + "."
        bas_sol['_eTNP_2'] = contents[n + 7:n + 9] + "."
        bas_sol['_eTNP_3'] = contents[n + 9:n + 11] + "."

    n = contents.find("_avo", 66)
    if n != -1:
        bas_sol['_avo'] = contents[n + 4:n + 8]
        bas_sol['_avo_1'] = contents[n + 8:n + 9] + "." + contents[n + 9:n + 12]
        bas_sol['_avo_2'] = contents[n + 12:n + 13] + "." + contents[n + 13:n + 16]

    n = contents.find("_cvo", 66)
    if n != -1:
        bas_sol['_cvo'] = contents[n + 4:n + 8]
        bas_sol['_cvo_1'] = contents[n + 8:n + 9] + "." + contents[n + 9:n + 12]
        bas_sol['_cvo_2'] = contents[n + 12:n + 13] + "." + contents[n + 13:n + 16]

    n = contents.find("_pola", 66)
    if n != -1:
        bas_sol['_pola_1'] = contents[n + 5:n + 9]
        bas_sol['_pola_2'] = contents[n + 9:n + 10] + "." + contents[n + 10:n + 13]

    n = contents.find("_runID", 66)
    if n != -1:
        bas_sol['_runID'] = contents[n + 6:n + 17]

    print(bas_sol)


def list_files(path):
    lf = os.listdir(path)
    return lf


if __name__ == "__main__":
    main()
