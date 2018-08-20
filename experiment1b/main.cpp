//
//  main.cpp
//  OpenCVTest
//
//  Created by Harsha Kenchareddy on 8/19/18.
//  Copyright © 2018 Harsha Kenchareddy. All rights reserved.
//

#include <iostream>
#include <opencv2/opencv.hpp>
#include <stdio.h>
#include <unistd.h>

using namespace cv;
using namespace std;

int ct = 0;
char tipka;
char filename[200]; // For filename
int  c = 1; // For filename

//int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    //return 0;
//}
int main(int, char**)
{
    
    
    Mat frame;
    //--- INITIALIZE VIDEOCAPTURE
    VideoCapture cap;
    // open the default camera using default API
    cap.open(0);
    // OR advance usage: select any API backend
    int deviceID = 0;             // 0 = open default camera
    int apiID = cv::CAP_ANY;      // 0 = autodetect default API
    // open selected camera using selected API
    cap.open(deviceID + apiID);
    // check if we succeeded
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    //--- GRAB AND WRITE LOOP
    cout << "Start grabbing" << endl
    << "Press a to terminate" << endl;
    for (;;)
    {
        // wait for a new frame from camera and store it into 'frame'
        cap.read(frame);
        
        if (frame.empty()) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }
        
        cout << "Start Sleep" << endl;
        usleep(5000000); // Sleep is mandatory - for no leg!
        cout << "End Sleep" << endl;
        
        
        // show live and wait for a key with timeout long enough to show images
        imshow("CAMERA 1", frame);  // Window name
        
        
        tipka = cv::waitKey(100);
        
        
        if (tipka == 'q') {
            cout << "Frame "<< c << endl;
            sprintf(filename, "/Users/harshak/projects/videomob/src/Frame_%d.jpg", c); // select your folder - filename is "Frame_n"qa
            cv::waitKey(10);
            
            imshow("CAMERA 1", frame);
            imwrite(filename, frame);
            cout << "Frame_" << c << endl;
            c++;
        }
        
        
        if (tipka == 'a') {
            cout << "Terminating..." << endl;
            usleep(2000);
            break;
        }
        
        
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}

