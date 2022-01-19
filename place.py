# -*- coding: utf-8 -*-
# Coded By İsmail Konak
# Mail: i_konak@hotmail.com

import os

def first():
  def search(list, file):
    for i in range(len(list)):
      if list[i] == file:
        return True
    return False
  konumfull = os.getcwd()
  konumfull = konumfull.split("\\")
  konum = f"{konumfull[0]}\{konumfull[1]}\{konumfull[2]}\{konumfull[3]}\{konumfull[4]}\\"
  print(konum)
  files_check = os.listdir(konum)
  if search(files_check,"values") is True:
    print("var")
  else:
    os.mkdir(f"{konum}\\values")


def idwrite(id):
  konumfull = os.getcwd()
  konumfull = konumfull.split("\\")
  konum = f"{konumfull[0]}\{konumfull[1]}\{konumfull[2]}\{konumfull[3]}\{konumfull[4]}\\values\\id.py"
  with open(konum,"w+") as f:
    f.write(f"{id}")
    f.close()


def hsvLwrite(hsvL):
  konumfull = os.getcwd()
  konumfull = konumfull.split("\\")
  konum = f"{konumfull[0]}\{konumfull[1]}\{konumfull[2]}\{konumfull[3]}\{konumfull[4]}\\values\\hsvL.py"
  with open(konum,"w+") as f:
    f.write(f"{hsvL}")
    f.close()


def hsvHwrite(hsvH):
  konumfull = os.getcwd()
  konumfull = konumfull.split("\\")
  konum = f"{konumfull[0]}\{konumfull[1]}\{konumfull[2]}\{konumfull[3]}\{konumfull[4]}\\values\\hsvH.py"
  with open(konum,"w+") as f:
    f.write(f"{hsvH}")
    f.close()


def idread():
  konumfull = os.getcwd()
  konumfull = konumfull.split("\\")
  konum = f"{konumfull[0]}\{konumfull[1]}\{konumfull[2]}\{konumfull[3]}\{konumfull[4]}\\values\\id.py"
  with open(konum,"r+") as f:
    id_no = f.read()
    f.close()
  return id_no


def hsvLread():
  konumfull = os.getcwd()
  konumfull = konumfull.split("\\")
  konum = f"{konumfull[0]}\{konumfull[1]}\{konumfull[2]}\{konumfull[3]}\{konumfull[4]}\\values\\hsvL.py"
  with open(konum,"r+") as f:
    hsv_low = f.read()
    hsv_low = hsv_low.split(",")
    f.close()
  return hsv_low


def hsvHread():
  konumfull = os.getcwd()
  konumfull = konumfull.split("\\")
  konum = f"{konumfull[0]}\{konumfull[1]}\{konumfull[2]}\{konumfull[3]}\{konumfull[4]}\\values\\hsvH.py"
  with open(konum,"r+") as f:
    hsv_high = f.read()
    hsv_high = hsv_high.split(",")
    f.close()
  return hsv_high


if __name__ == "__main__":
  first()
  idread()
  hsvHread()
  hsvLread()