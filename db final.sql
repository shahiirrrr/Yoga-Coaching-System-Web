/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - yoga
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`yoga` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `yoga`;

/*Table structure for table `assignwork_table` */

DROP TABLE IF EXISTS `assignwork_table`;

CREATE TABLE `assignwork_table` (
  `ASSIGNEDWORK_ID` int(11) NOT NULL AUTO_INCREMENT,
  `TRAINER_ID` int(11) DEFAULT NULL,
  `WORK_ID` int(11) DEFAULT NULL,
  `DATE` varchar(10) NOT NULL,
  `STATUS` varchar(100) NOT NULL,
  PRIMARY KEY (`ASSIGNEDWORK_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `assignwork_table` */

insert  into `assignwork_table`(`ASSIGNEDWORK_ID`,`TRAINER_ID`,`WORK_ID`,`DATE`,`STATUS`) values 
(1,NULL,1,'','pending'),
(2,NULL,0,'',''),
(3,NULL,3,'',''),
(4,0,0,'2022-12-22','Assigned'),
(5,5,2,'2022-12-22','Assigned'),
(6,6,5,'2022-12-22','Assigned'),
(8,2,5,'2022-12-23','Assigned'),
(9,6,5,'2022-12-23','Assigned'),
(10,4,8,'2022-12-28','completed');

/*Table structure for table `compaint_table` */

DROP TABLE IF EXISTS `compaint_table`;

CREATE TABLE `compaint_table` (
  `COMPLAINT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` int(11) DEFAULT NULL,
  `TID` int(11) DEFAULT NULL,
  `COMPLAINT` text,
  `REPLY` varchar(100) DEFAULT NULL,
  `DATE` varchar(10) NOT NULL,
  PRIMARY KEY (`COMPLAINT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `compaint_table` */

insert  into `compaint_table`(`COMPLAINT_ID`,`USER_ID`,`TID`,`COMPLAINT`,`REPLY`,`DATE`) values 
(1,7,4,'very bad trainer\r\n','DCDCF','12/12/12'),
(2,3,5,'gjgjggg',NULL,''),
(3,2,5,' yehmxk','hallo','2022-12-27'),
(4,2,4,' sbbwnj','','2022-12-27'),
(5,2,4,' jj','gaffa','2022-12-27'),
(6,2,0,' ','pending','2022-12-27'),
(7,2,0,' heben','pending','2022-12-27'),
(8,1,4,' jjannj','','2022-12-28'),
(9,1,4,' gjgh','pending','2022-12-28');

/*Table structure for table `doubt_table` */

DROP TABLE IF EXISTS `doubt_table`;

CREATE TABLE `doubt_table` (
  `DOUBT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` int(11) DEFAULT NULL,
  `TRAINER_ID` int(11) DEFAULT NULL,
  `DOUBT` varchar(500) DEFAULT NULL,
  `REPLY` varchar(500) DEFAULT NULL,
  `DATE` varchar(10) NOT NULL,
  PRIMARY KEY (`DOUBT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `doubt_table` */

insert  into `doubt_table`(`DOUBT_ID`,`USER_ID`,`TRAINER_ID`,`DOUBT`,`REPLY`,`DATE`) values 
(1,4,6,'hbjrfhgdrhgfr','hjbsdhjbd',''),
(2,2,5,'fnnanakn','h jsjbd',''),
(3,2,4,' yuegsg','abc','2022-12-27'),
(4,2,4,' ghff','admin','2022-12-27'),
(5,2,4,' ggddjirgsujd','abc','2022-12-27'),
(6,2,4,' 5gwye','hhhh','2022-12-27'),
(7,2,5,' ushbbbb','pending','2022-12-28');

/*Table structure for table `expert_table` */

DROP TABLE IF EXISTS `expert_table`;

CREATE TABLE `expert_table` (
  `EXPERT_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` int(11) DEFAULT NULL,
  `FIRST_NAME` varchar(15) DEFAULT NULL,
  `LAST_NAME` varchar(15) DEFAULT NULL,
  `GENDER` varchar(10) NOT NULL,
  `PHONE` varchar(15) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `QUALIFICATION` varchar(50) NOT NULL,
  PRIMARY KEY (`EXPERT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `expert_table` */

/*Table structure for table `login_table` */

DROP TABLE IF EXISTS `login_table`;

CREATE TABLE `login_table` (
  `LOGIN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_NAME` varchar(20) NOT NULL,
  `PASSWORD` varchar(10) NOT NULL,
  `TYPE` varchar(50) NOT NULL,
  PRIMARY KEY (`LOGIN_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login_table` */

insert  into `login_table`(`LOGIN_ID`,`USER_NAME`,`PASSWORD`,`TYPE`) values 
(1,'anu','sree ','user'),
(2,'000','000 ','user'),
(3,'123','123','trainer'),
(4,'admin','1234','trainer'),
(5,'Sufiyan','4112','admin'),
(6,'fggjj',' jiji','user');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `tid` int(11) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`rid`,`uid`,`tid`,`date`,`status`) values 
(1,2,5,'2022-12-27','accepted'),
(2,2,4,'2022-12-27','rejected'),
(3,2,4,'2022-12-27','accepted'),
(4,2,4,'2022-12-28','pending'),
(5,1,4,'2022-12-28','pending'),
(6,1,4,'2022-12-28','accepted'),
(7,1,4,'2022-12-28','pending');

/*Table structure for table `time_table` */

DROP TABLE IF EXISTS `time_table`;

CREATE TABLE `time_table` (
  `TIME_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` int(11) DEFAULT NULL,
  `DATE` varchar(10) NOT NULL,
  `SLOAT` varchar(50) NOT NULL,
  PRIMARY KEY (`TIME_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `time_table` */

/*Table structure for table `trainer_table` */

DROP TABLE IF EXISTS `trainer_table`;

CREATE TABLE `trainer_table` (
  `TRAINER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `LOGIN_ID` int(11) DEFAULT NULL,
  `FIRST_NAME` varchar(15) DEFAULT NULL,
  `LAST_NAME` varchar(15) DEFAULT NULL,
  `GENDER` varchar(10) NOT NULL,
  `DOB` varchar(10) NOT NULL,
  `PHONE` varchar(15) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `QUALIFICATION` varchar(50) NOT NULL,
  PRIMARY KEY (`TRAINER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `trainer_table` */

insert  into `trainer_table`(`TRAINER_ID`,`LOGIN_ID`,`FIRST_NAME`,`LAST_NAME`,`GENDER`,`DOB`,`PHONE`,`EMAIL`,`QUALIFICATION`) values 
(5,4,'admin','cheyanam','Male','1980-01-01','7892343235','aswinpr2004@gmail.com','degree');

/*Table structure for table `user_table` */

DROP TABLE IF EXISTS `user_table`;

CREATE TABLE `user_table` (
  `USER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `LOGIN_ID` int(11) DEFAULT NULL,
  `FIRST_NAME` varchar(20) DEFAULT NULL,
  `LAST_NAME` varchar(20) DEFAULT NULL,
  `GENDER` varchar(10) NOT NULL,
  `DOB` varchar(15) NOT NULL,
  `PHONE` varchar(15) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `HEIGHT` varchar(10) NOT NULL,
  `WEIGHT` varchar(10) NOT NULL,
  `HEALTH_DISCRIPTION` varchar(100) NOT NULL,
  PRIMARY KEY (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `user_table` */

insert  into `user_table`(`USER_ID`,`LOGIN_ID`,`FIRST_NAME`,`LAST_NAME`,`GENDER`,`DOB`,`PHONE`,`EMAIL`,`HEIGHT`,`WEIGHT`,`HEALTH_DISCRIPTION`) values 
(2,2,' supyan',' mohd','Male','22/01/2002','62385649',' sufiyanmuhammedms@gmail.com','170','70','good'),
(14,1,' anu',' sree','Female','27-01-2001','9638527412',' anu@gmail.com','157','52','good'),
(16,6,' 688',' fhb','Female','fghh','5866544',' ffsjk','tghh','gfghj','fgh'),
(17,7,' ',' ','Other','','',' ','','',''),
(18,8,' ',' ','Other','','',' ','','',''),
(19,9,' ',' ','Female','','',' ','','',''),
(20,10,' ',' ','Female','12/28/22','9468464698',' jiji@gmail.com','hbb','gbj',''),
(21,11,'',' ','Male','12/28/22','6975846349',' uangan','hsv','ghsb','bsbj');

/*Table structure for table `video_table` */

DROP TABLE IF EXISTS `video_table`;

CREATE TABLE `video_table` (
  `VIDEO_ID` int(11) NOT NULL AUTO_INCREMENT,
  `trainer_id` int(11) DEFAULT NULL,
  `VIDEO` varchar(50) DEFAULT NULL,
  `DESCRIPTION` varchar(50) DEFAULT NULL,
  `DATE` varchar(10) NOT NULL,
  PRIMARY KEY (`VIDEO_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `video_table` */

insert  into `video_table`(`VIDEO_ID`,`trainer_id`,`VIDEO`,`DESCRIPTION`,`DATE`) values 
(1,2,'IMG-20211101-WA0301.jpg','cm college','2022-12-22'),
(3,6,'B612_20180616_163646_807.jpg','','2022-12-22'),
(4,4,'B612_20180616_163646_807.jpg','aswim','2022-12-28'),
(7,4,'PXL_20220923_103802496.mp4','qwertyui','2022-12-28');

/*Table structure for table `work_table` */

DROP TABLE IF EXISTS `work_table`;

CREATE TABLE `work_table` (
  `WORK_ID` int(11) NOT NULL AUTO_INCREMENT,
  `WORKS` varchar(50) NOT NULL,
  `DETAILS` text NOT NULL,
  `work_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`WORK_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `work_table` */

insert  into `work_table`(`WORK_ID`,`WORKS`,`DETAILS`,`work_date`) values 
(5,'aswin123','cheyanam',NULL),
(6,'abc','mohmd',NULL),
(7,'hgdskfhjefjhg','fdcdc',NULL),
(8,'qwertyu','wertyuio','2022-12-28');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
