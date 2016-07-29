#include "opencv2/opencv.hpp"
#include <sstream>
#include <iostream>
using namespace cv;
using namespace std;

 Mat frame,img;
 int counter,i;

int main(int,char**)
 {
  VideoCapture vid("0.mov");
  cout << "Video opened!" << endl;

 while(1){
    stringstream file;
    vid.read(frame);
    transpose(frame, frame);
     flip(frame, frame, 1);
    if(frame.empty()) break;
        counter++;
    if(counter%2==0) {
    i++;
    file <<  i << ".jpg";
    imwrite(file.str(),frame);
    }

}
}
