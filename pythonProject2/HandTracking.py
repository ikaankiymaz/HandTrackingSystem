import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) !=0:

        ortaFinger1X = lmList[12][1]
        ortaFinger1Y = lmList[12][2]
        ortaFinger2X = lmList[11][1]
        ortaFinger2Y = lmList[11][2]
        ortaFinger3X = lmList[10][1]
        ortaFinger3Y = lmList[10][2]
        ortaFinger4X = lmList[9][1]
        ortaFinger4Y = lmList[9][2]

        isaretFinger1X = lmList[8][1]
        isaretFinger1Y = lmList[8][2]
        isaretFinger2X = lmList[7][1]
        isaretFinger2Y = lmList[7][2]
        isaretFinger3X = lmList[6][1]
        isaretFinger3Y = lmList[6][2]
        isaretFinger4X = lmList[5][1]
        isaretFinger4Y = lmList[5][2]

        basFinger1X = lmList[4][1]
        basFinger1Y = lmList[4][2]
        basFinger2X = lmList[3][1]
        basFinger2Y = lmList[3][2]
        basFinger3X = lmList[2][1]
        basFinger3Y = lmList[2][2]

        yuzukFinger1X = lmList[16][1]
        yuzukFinger1Y = lmList[16][2]
        yuzukFinger2X = lmList[15][1]
        yuzukFinger2Y = lmList[15][2]
        yuzukFinger3X = lmList[14][1]
        yuzukFinger3Y = lmList[14][2]
        yuzukFinger4X = lmList[13][1]
        yuzukFinger4Y = lmList[13][2]

        serceFinger1X = lmList[20][1]
        serceFinger1Y = lmList[20][2]
        serceFinger2X = lmList[19][1]
        serceFinger2Y = lmList[19][2]
        serceFinger3X = lmList[18][1]
        serceFinger3Y = lmList[18][2]
        serceFinger4X = lmList[17][1]
        serceFinger4Y = lmList[17][2]


        #print(bas parmak 1x , lmList[4][1], isaret parmagi 1x, lmList[8][1], bas parmak 1y , lmList[4][2], isaret parmagi 1y, lmList[8][2])

        #print("bas parmak   1x:", basFinger1X, "bas parmak   1y:", basFinger1Y, "bas parmak   2x:" , basFinger2X, "bas parmak   2y:", basFinger2Y,
        #      "bas parmak   3x:", basFinger3X, "bas parmak   3y:", basFinger3Y)

        #print("isaret parmak1x:", isaretFinger1X, "isaret parmak1y:", isaretFinger1Y, "isaret parmak2x:", isaretFinger2X, "isaret parmak2y:", isaretFinger2Y,
        #      "isaret parmak3x:", isaretFinger3X, "isaret parmak3y:", isaretFinger3Y, "isaret parmak4x:", isaretFinger4X, "isaret parmak4y:", isaretFinger4Y)

        print("orta parmak  1x:", ortaFinger1X, "orta parmak  1y:", ortaFinger1Y, "orta parmak  2x:", ortaFinger2X, "orta parmak  2y:", ortaFinger2Y,
              "orta parmak  3x:", ortaFinger3X, "orta parmak  3y:", ortaFinger3Y, "orta parmak  4x:", ortaFinger4X, "orta parmak  4y:", ortaFinger4Y)

        print("yuzuk parmak 1x:", yuzukFinger1X, "yuzuk parmak 1y:", yuzukFinger1Y, "yuzuk parmak 2x:", yuzukFinger2X, "yuzuk parmak 2y:", yuzukFinger2Y,
               "yuzuk parmak 3x:", yuzukFinger3X, "yuzuk parmak 3y:", yuzukFinger3Y, "yuzuk parmak 4x:", yuzukFinger4X, "yuzuk parmak 4y:", yuzukFinger4Y)

        print("serce parmak 1x:", serceFinger1X, "serce parmak 1y:", serceFinger1Y, "serce parmak 2x:", serceFinger2X, "serce parmak 2y:", serceFinger2Y,
              "serce parmak 3x:", serceFinger3X, "serce parmak 3y:", serceFinger3Y, "serce parmak 4x:", serceFinger4X, "serce parmak 4y:", serceFinger4Y)

        #print(orta parmak 1x , ortaFinder1X, orta parmak 1y, ortaFinder1Y, isaret parmak 1x , isaretFinger1X, isaret parmak 1y, isaretFinger1Y,
        #      yuzuk parmak 1x , yuzukFinger1X, yuzuk parmak 1y, yuzukFinger1Y, serce parmak 1x , serceFinger1X, serce parmak 1y, serceFinger1Y)


        #if(((ortaFinder4X-ortaFinder3X)  9  and (ortaFinder4X-ortaFinder3X)  11 and (ortaFinder4X-ortaFinder2X)  13 and (ortaFinder4X-ortaFinder1X)  15) and
        #    (isaretFinger1Y - ortaFinder1Y)  70 and (yuzukFinger1Y - ortaFinder1Y)  70 and (serceFinger1Y - ortaFinder1Y)  50)


        if ((((((basFinger1X - isaretFinger1X) < 30) or ((isaretFinger1X - basFinger1X) < 30)) and (basFinger1Y - isaretFinger1Y < 30)) and (isaretFinger3X - basFinger2X < 70) and ((basFinger2Y - isaretFinger3Y > -10))) and
            (((isaretFinger1Y - ortaFinger1Y) > 20) and ((isaretFinger1Y - yuzukFinger1Y) > 5))):
            #print(OKEY ISARETI)
            cv2.putText(img, "OKEY", (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        elif(((ortaFinger4X-ortaFinger3X) < 40 and (ortaFinger4X-ortaFinger2X) < 60 and (ortaFinger4X-ortaFinger1X) < 80) and
             (isaretFinger2Y - ortaFinger2Y > 50 and (isaretFinger1Y - isaretFinger3Y > 10)) and ((isaretFinger1Y - ortaFinger1Y) > 70 and (yuzukFinger1Y - ortaFinger1Y) > 75 and (serceFinger1Y - ortaFinger1Y) > 75)):
            #print("KARDESIM AYIP DEGIL MI")
            cv2.putText(img, "AHLAKSIZ ADAM", (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        elif (((isaretFinger4X - isaretFinger3X) < 40 and (isaretFinger4X - isaretFinger2X) < 60 and (isaretFinger4X - isaretFinger1X) < 80) and
              ((ortaFinger1Y - isaretFinger1Y) > 45 and (yuzukFinger1Y - isaretFinger1Y) > 45 and (serceFinger1Y - isaretFinger1Y) > 45)):
            #print(BIR)
            cv2.putText(img, "BIR", (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        elif(((ortaFinger1X - isaretFinger1X >20) or (isaretFinger1X - ortaFinger1X > 20)) and ((ortaFinger2X - isaretFinger2X >15) or (isaretFinger2X - ortaFinger2X > 15)) and
            ((serceFinger1Y - isaretFinger1Y > 60) and (yuzukFinger1Y - isaretFinger1Y > 60) and (basFinger1Y - isaretFinger1Y > 45)) and ((serceFinger1Y - ortaFinger1Y > 60) and (yuzukFinger1Y - ortaFinger1Y > 60) and (basFinger1Y - ortaFinger1Y > 45))):
            cv2.putText(img, "IKI", (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        elif(((ortaFinger1X - isaretFinger1X > 20) or (isaretFinger1X - ortaFinger1X > 20)) and ((ortaFinger2X - isaretFinger2X > 15) or (isaretFinger2X - ortaFinger2X > 15)) and
            ((serceFinger1Y - isaretFinger1Y > 40) and (basFinger1Y - isaretFinger1Y > 40)) and ((serceFinger1Y - ortaFinger1Y > 40)  and (basFinger1Y - ortaFinger1Y > 40)) and ((serceFinger1Y - yuzukFinger1Y > 40) and (basFinger1Y - yuzukFinger1Y > 40)) and
             ((serceFinger1X - basFinger1X < 40) or (basFinger1X - serceFinger1X < 50))):
            cv2.putText(img, "UC", (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        elif(((ortaFinger1X - isaretFinger1X > 20) or (isaretFinger1X - ortaFinger1X > 20)) and ((ortaFinger2X - isaretFinger2X > 15) or (isaretFinger2X - ortaFinger2X > 15)) and
            ((ortaFinger1X - yuzukFinger1X > 20) or (yuzukFinger1X - ortaFinger1X > 20)) and ((ortaFinger2X - yuzukFinger2X > 20) or (yuzukFinger2X - ortaFinger2X > 20)) and
            ((serceFinger1X - yuzukFinger1X > 25) or (yuzukFinger1X - serceFinger1X > 25)) and ((serceFinger2X - yuzukFinger2X > 25) or (yuzukFinger2X - serceFinger2X > 25)) and
            ((isaretFinger1X - yuzukFinger1X > 40) or (yuzukFinger1X - isaretFinger1X > 40)) and ((isaretFinger1X - serceFinger1X > 50) or (serceFinger1X - isaretFinger1X > 50)) and
            ((serceFinger4X - basFinger1X < 70)) and ((basFinger1Y - isaretFinger1Y > 40) and (basFinger1Y - ortaFinger1Y > 40) and (basFinger1Y - yuzukFinger1Y > 40) and (basFinger1Y - serceFinger1Y > 35))):
            cv2.putText(img, "DORT", (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        else:
            #print(SERBEST)
            cv2.putText(img, "SERBEST", (250, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        #for i in lmList
            #print(range(i[0], i[1], i[2]))



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str((fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()