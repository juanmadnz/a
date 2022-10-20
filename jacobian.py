import numpy as np

MAX_STEP = 10

class JacobianController:
    def __init__(self, arm):
        # the controller should save a reference to the arm it's controlling
        self.arm = arm

    def control(self, target):
        if self.arm.get_num_joints() == 6:
            # if arm has 6 joints
            self.control6J6D(target)
        else:
            raise Exception("JacobianController.control(target): Can't control an arm with this amount joints.")

    def control6J6D(self, target):
        # the control method receives a target
        curr_end = self.arm.endeffector()
        delta_pos = target - curr_end
        # we limit the size of the delta_pos vector as MAX_STEP
        # to avoid making large steps
        if delta_pos.r > MAX_STEP:
            delta_pos.r = MAX_STEP

        # # calculate the inverse Jacobian matrix
        # iJ = 1/(self.arm.lengths[0]*self.arm.lengths[1]*np.sin(self.arm.thetas[1])) * np.array([
        # [self.arm.lengths[1]*np.cos(self.arm.thetas[0] + self.arm.thetas[1]),
        #  self.arm.lengths[1]*np.sin(self.arm.thetas[0] + self.arm.thetas[1])],
        # [-self.arm.lengths[0]*np.cos(self.arm.thetas[0])-self.arm.lengths[1]*np.cos(self.arm.thetas[0]+self.arm.thetas[1]),
        #  -self.arm.lengths[0]*np.sin(self.arm.thetas[0])-self.arm.lengths[1]*np.sin(self.arm.thetas[0]+self.arm.thetas[1])]
        # ])

        t0 = self.arm.thetas[0]
        t1 = self.arm.thetas[1]
        t2 = self.arm.thetas[2]
        t3 = self.arm.thetas[3]
        t4 = self.arm.thetas[4]
        t5 = self.arm.thetas[5]

        l0 = self.arm.lengths[0]
        l1 = self.arm.lengths[1]
        l2 = self.arm.lengths[2]
        l3 = self.arm.lengths[3]
        l4 = self.arm.lengths[4]
        l5 = self.arm.lengths[5]

        a00 = (100*((-(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*(((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.cos(t5) + (100*((-(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) + 100*(-((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.sin(t5) + (100*(-(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + (100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4) + (100*(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + (100*(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + 100*(np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + (100*np.sin(t0)*np.sin(t1) - 100*np.cos(t0)*np.cos(t1))*np.sin(t2) + (-100*np.sin(t0)*np.cos(t1) - 100*np.sin(t1)*np.cos(t0))*np.cos(t2) - 100*np.sin(t0)*np.cos(t1) - 100*np.sin(t0) - 100*np.sin(t1)*np.cos(t0)
        a01 = (100*((-(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*(((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.cos(t5) + (100*((-(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) + 100*(-((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.sin(t5) + (100*(-(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + (100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4) + (100*(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + (100*(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) + 100*(np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + (100*np.sin(t0)*np.sin(t1) - 100*np.cos(t0)*np.cos(t1))*np.sin(t2) + (-100*np.sin(t0)*np.cos(t1) - 100*np.sin(t1)*np.cos(t0))*np.cos(t2) - 100*np.sin(t0)*np.cos(t1) - 100*np.sin(t1)*np.cos(t0)
        a02 = (100*(-(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4) + 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4))*np.sin(t5) + (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4) + 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4))*np.cos(t5) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4) + (100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + (-100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + (100*(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.cos(t2) - 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) - (-100*np.sin(t0)*np.sin(t1) + 100*np.cos(t0)*np.cos(t1))*np.sin(t2) + (-100*np.sin(t0)*np.cos(t1) - 100*np.sin(t1)*np.cos(t0))*np.cos(t2)
        a03 = (100*(-(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + (-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.cos(t5) + (100*(-(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + (-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) + 100*(-(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.sin(t5) + (-100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4) + (-100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - (100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3)
        a04 = (100*(-(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) - 100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.sin(t5) + (-100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.cos(t5) - (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4)
        a05 = (-100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.cos(t5) - (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) + 100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.sin(t5)
        a10 = (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3))*np.sin(t4) + 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3))*np.cos(t4))*np.cos(t5) + (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3))*np.cos(t4) + 100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) - ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3))*np.sin(t4))*np.sin(t5) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3))*np.sin(t4) + (100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3))*np.cos(t4) + (100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) + (100*(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + (-100*np.sin(t0)*np.sin(t1) + 100*np.cos(t0)*np.cos(t1))*np.cos(t2) + (-100*np.sin(t0)*np.cos(t1) - 100*np.sin(t1)*np.cos(t0))*np.sin(t2) - 100*np.sin(t0)*np.sin(t1) + 100*np.cos(t0)*np.cos(t1) + 100*np.cos(t0)
        a11 = (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3))*np.sin(t4) + 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3))*np.cos(t4))*np.cos(t5) + (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3))*np.cos(t4) + 100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) - ((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3))*np.sin(t4))*np.sin(t5) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3))*np.sin(t4) + (100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) + 100*((np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3))*np.cos(t4) + (100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) + (100*(np.sin(t0)*np.sin(t1) - np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + (-100*np.sin(t0)*np.sin(t1) + 100*np.cos(t0)*np.cos(t1))*np.cos(t2) + (-100*np.sin(t0)*np.cos(t1) - 100*np.sin(t1)*np.cos(t0))*np.sin(t2) - 100*np.sin(t0)*np.sin(t1) + 100*np.cos(t0)*np.cos(t1)
        a12 = (100*(-(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + (-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.sin(t5) + (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) + 100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + (-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.cos(t5) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + 100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4) + (-100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(-np.sin(t0)*np.cos(t1) - np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + (100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - 100*(np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3) + (-100*np.sin(t0)*np.sin(t1) + 100*np.cos(t0)*np.cos(t1))*np.cos(t2) - (100*np.sin(t0)*np.cos(t1) + 100*np.sin(t1)*np.cos(t0))*np.sin(t2)
        a13 = (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4) + 100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4))*np.cos(t5) + (100*((-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4) + 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4))*np.sin(t5) + (100*(-(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4) + (-100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) - (100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + 100*(np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + (100*(-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - 100*(np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3)
        a14 = (-100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) - ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.sin(t5) + (100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) - 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.cos(t5) + (-100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) - (100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + 100*((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4)
        a15 = -(100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.sin(t4) + 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.cos(t4))*np.sin(t5) + (100*(-((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.sin(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.cos(t3))*np.cos(t4) - 100*(((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.sin(t2) + (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.cos(t2))*np.cos(t3) + ((-np.sin(t0)*np.sin(t1) + np.cos(t0)*np.cos(t1))*np.cos(t2) - (np.sin(t0)*np.cos(t1) + np.sin(t1)*np.cos(t0))*np.sin(t2))*np.sin(t3))*np.sin(t4))*np.cos(t5)



        J = np.array([[a00, a01, a02, a03, a04, a05],[a10, a11, a12, a13, a14, a15]])
        iJ = np.linalg.pinv(J)

        # the dot product between iJ and the desired displacement
        # in the end-effector gives us the change necessary in joint values
        delta_joints = iJ.dot(np.array([delta_pos.x, delta_pos.y]))

        # with delta_joints in hand, we move the arm
        self.arm.move(delta_joints)
        pass
