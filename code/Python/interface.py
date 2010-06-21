from stereoheader import *

def menu():
  """
  Shows simple interface to work with the stereo vision project.
  """
  choice = ""
  while not choice == "q":
    print "== STEREO CALIBRATION =="
    print "1. Get chessboard points from cam"
    print "2. Get image pair from cam"
    print "3. Generate calibration parameters from chessboard points in file"
    print "4. Generate rectification parameters from calibration parameters"
    print "5. Rectify images"
    print "q. Exit"

    choice = raw_input("> ")

    if not ((choice.isdigit() and (1 <= int(choice) <= 5)) or choice == "q"):
      print "Please enter a choice between 1 and 5, or q to quit."
      continue

    if choice == "1":
      (c1, c2) = genCamWindows("Camera 1", "Camera 2")
      writeChessboards(c1, c2, "Camera 1", "Camera 2")
      continue

    if choice == "2":
      getStereoImages()
      continue

    if choice == "3":
      saveCalibration(stereoCalibrate(8, "chessboards.txt"), "calib")
      continue

    if choice == "4":
      saveRectif(stereoRectify())
      continue

    if choice == "5":
      im1 = cv.LoadImageM("im1.bmp")
      im2 = cv.LoadImageM("im2.bmp")
      rectifyImages(im1, im2)
      continue

    if choice == "q":
      print "Exiting."
      break

if __name__ == "__main__":
  menu()
