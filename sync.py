import cv2

cap1 = cv2.VideoCapture('0218_part1.mp4')
cap2 = cv2.VideoCapture('0218_part2.mp4')

frame1 = int(round(cap1.get(cv2.CAP_PROP_FPS), 0))
frame2 = int(round(cap2.get(cv2.CAP_PROP_FPS), 0))


fram_list1 = [1] * frame1
fram_list2 = [1] * frame2

def findone(list):
    count = []
    for i, value in enumerate(list):
        if value == 1:
            count.append(i)
    return count


def sync():
    a = fram_list1.count(1)
    b = fram_list2.count(1)

    if a == b:
        return None
    else:
        dif = abs(a - b)

        if dif == 1:
            if a > b:
                one_loc = findone(fram_list1)
                fram_list1[one_loc[-1]] = 0
            else:
                one_loc = findone(fram_list2)
                fram_list2[one_loc[-1]] = 0


        else:
            i = max(a, b) // dif
            if i == 1:
                i += 1

            if a > b:
                one_loc = findone(fram_list1)
                for j in range(i - 1, len(one_loc), i):
                    fram_list1[one_loc[j]] = 0
            else:
                one_loc = findone(fram_list2)
                for j in range(i - 1, len(one_loc), i):
                    fram_list2[one_loc[j]] = 0
    sync()


if fram_list1.count(1) != fram_list2.count(1):
    sync()
else:
    print("There is no change")
