#include <iostream>
#include <omni_kinematics/omnipointer.hpp>
#include <omni_kinematics/omnigrasper.hpp>

int main(int argc, char** argv)
{
    Eigen::Vector4d joints(M_PI, M_PI, M_PI, M_PI);
    double x = 0;
    double y = 0;
    double theta = 0;

    if (argc >= 8)
    {
        x = atof(argv[1]);
        y = atof(argv[2]);
        theta = atof(argv[3]);
        joints[0] = atof(argv[4]);
        joints[1] = atof(argv[5]);
        joints[2] = atof(argv[6]);
        joints[3] = atof(argv[7]);
    }
    else if (argc >= 5)
    {
        joints[0] = atof(argv[1]);
        joints[1] = atof(argv[2]);
        joints[2] = atof(argv[3]);
        joints[3] = atof(argv[4]);
    }

    std::cout << "Omnipointer end effector position (with respect to the arm frame): " << omni_kinematics::Omnipointer::arm_forward_model(joints).transpose() << std::endl;    
    std::cout << "Omnipointer end effector position (with respect to the base frame before base movement): " << omni_kinematics::Omnipointer::full_forward_model(x, y, theta, joints).transpose() << std::endl;    
    std::cout << "Omnigrasper end effector position (with respect to the arm frame): " << omni_kinematics::Omnigrasper::arm_forward_model(joints).transpose() << std::endl;
    std::cout << "Omnipointer end effector position (with respect to the base frame before base movement): " << omni_kinematics::Omnipointer::full_forward_model(x, y, theta, joints).transpose() << std::endl;    
    return 0;
}