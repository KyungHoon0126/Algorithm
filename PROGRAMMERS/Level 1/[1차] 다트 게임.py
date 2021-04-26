import re as regex
import math

test_case = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']


def solution(dartResult):
    dart_sums = [0 for i in range(3)]
    dart_results = regex.compile('[0-9]+[SDT]{1}[#*]?').findall(dartResult)

    for idx, i in enumerate(dart_results):
        dart_results[idx] = i.replace('S', '1').replace('D', '2').replace('T', '3').replace('10', 'K')

    for idx, dart in enumerate(dart_results):
        if len(dart) > 2:
            for j in dart:
                temp = 0
                if dart[-1] == '*':
                    temp = math.pow(int(dart[0].replace('K', '10')), int(dart[1])) * 2
                    if idx == 1:
                        dart_sums[0] = dart_sums[0] * 2
                    elif idx == 2:
                        dart_sums[1] = dart_sums[1] * 2

                if dart[-1] == '#':
                    temp = math.pow(int(dart[0]), int(dart[1])) * -1

                dart_sums[idx] = temp
                break
        else:
            temp = math.pow(int(dart[0].replace('K', '10')), int(dart[1]))
            dart_sums[idx] = temp

    return int(sum(dart_sums))