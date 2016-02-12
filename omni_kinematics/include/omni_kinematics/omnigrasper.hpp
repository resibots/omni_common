#ifndef OMNI_KINEMATICS_OMNIGRASPER_HPP_
#define OMNI_KINEMATICS_OMNIGRASPER_HPP_

#include <math.h>

#include <Eigen/Core>

namespace omni_kinematics {
class Omnigrasper {
public:
    // Returns the position of the end-effector in the reference frame of the base, after the base movement
    static Eigen::Vector3d full_forward_model(double x, double y, double theta, const Eigen::Vector4d& joints)
    {
        // vrep: return arm_forward_model(joints) + Eigen::Vector3d(-0.008, 0.012, 0.0335);
        Eigen::Matrix3d base_rotation;
        base_rotation << cos(theta), -sin(theta), 0,
            sin(theta), cos(theta), 0,
            0, 0, 1;

        return (base_rotation * (arm_forward_model(joints) + Eigen::Vector3d(0.174917459488, 0, 0.167584627867))) + Eigen::Vector3d(x, y, 0);
    }

    // Returns the position of the end-effector in the reference frame of the arm
    static Eigen::Vector3d arm_forward_model(const Eigen::Vector4d& joints)
    {
        return (_arm_tr_mat(joints) * Eigen::Vector4d(0, 0, 0, 1)).head(3);
    }

protected:
    // Returns the full transformation matrix for the kinematic chain of the arm
    static Eigen::Matrix4d _arm_tr_mat(const Eigen::Vector4d& joints)
    {
        Eigen::MatrixXd dh = _dh_mat(joints);

        Eigen::Matrix4d mat = Eigen::Matrix4d::Identity(4, 4);

        for (size_t i = 0; i < dh.rows(); i++) {
            mat = mat * _trmat_dh(dh.row(i));
        }

        return mat;
    }

    // Returns a matrix containing the DH parameters (one row per joint)
    static Eigen::MatrixXd _dh_mat(const Eigen::VectorXd& q)
    {
        Eigen::MatrixXd dh(6, 4);

        dh << q(0) + M_PI, 0.086, 0, M_PI / 2,
            q(1) + M_PI / 2, 0, 0.264, 0,
            M_PI / 2, 0, 0.03022813797, 0,
            q(2) + M_PI, 0, 0.03022813797, 0,
            M_PI / 2, 0, 0.257956548576, 0,
            //q(3), 0, 0.231302842, 0;
            q(3), 0, 0.19, 0;

        return dh;
    }

    // Returns the transformation matrix given by a row of the DH matrix
    static Eigen::Matrix4d _trmat_dh(const Eigen::VectorXd& dh)
    {
        Eigen::Matrix4d submat;
        submat << cos(dh(0)), -cos(dh(3)) * sin(dh(0)), sin(dh(3)) * sin(dh(0)), dh(2) * cos(dh(0)),
            sin(dh(0)), cos(dh(3)) * cos(dh(0)), -sin(dh(3)) * cos(dh(0)), dh(2) * sin(dh(0)),
            0, sin(dh(3)), cos(dh(3)), dh(1),
            0, 0, 0, 1;
        return submat;
    }
};
}

#endif