cmake_minimum_required(VERSION 2.8)
project( opencv_samples )
set( srcfile ${CMAKE_SOURCE_DIR}/src)
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
 
add_executable( klt ${srcfile}/klt.cpp )
target_link_libraries( klt ${OpenCV_LIBS} )
add_executable( sift ${srcfile}/sift.cpp )
target_link_libraries( sift ${OpenCV_LIBS} )
add_executable( tojpg ${srcfile}/tojpg.cpp )
target_link_libraries( tojpg   ${OpenCV_LIBS} )



 
