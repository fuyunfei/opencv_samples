#include <opencv2/xfeatures2d.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <vector>

using namespace std;
using namespace cv;
  // 
  // now, you can no more create an instance on the 'stack', like in the tutorial
  // (yea, noticed for a fix/pr).
  // you will have to use cv::Ptr all the way down:
  //
int main(int argc,char *argv[]){
Mat img_1 = imread(argv[1], IMREAD_GRAYSCALE);
Mat img_2 = imread(argv[2], IMREAD_GRAYSCALE);
 
  cv::Ptr<Feature2D> f2d = xfeatures2d::SIFT::create();
  //cv::Ptr<Feature2D> f2d = xfeatures2d::SURF::create();
  //cv::Ptr<Feature2D> f2d = ORB::create();
  // you get the picture, i hope..

  //-- Step 1: Detect the keypoints:
  std::vector<KeyPoint> keypoints_1, keypoints_2;    
  f2d->detect( img_1, keypoints_1 );
  f2d->detect( img_2, keypoints_2 );

  //-- Step 2: Calculate descriptors (feature vectors)    
  Mat descriptors_1, descriptors_2;    
  f2d->compute( img_1, keypoints_1, descriptors_1 );
  f2d->compute( img_2, keypoints_2, descriptors_2 );

  //-- Step 3: Matching descriptor vectors using BFMatcher :
  BFMatcher matcher;
  std::vector< DMatch > matches;
  matcher.match( descriptors_1, descriptors_2, matches ); 
namedWindow("matches", 1);
Mat img_matches;
drawMatches(img_1, keypoints_1, img_2, keypoints_2, matches, img_matches);
imshow("matches", img_matches);
cv::imwrite("sift_result.jpg",  img_matches);


return 0;
}
