-- MySQL dump 10.13  Distrib 5.7.20, for macos10.12 (x86_64)
--
-- Host: localhost    Database: gatechecker_db
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add building',7,'add_building'),(26,'Can change building',7,'change_building'),(27,'Can delete building',7,'delete_building'),(28,'Can view building',7,'view_building'),(29,'Can add device',8,'add_device'),(30,'Can change device',8,'change_device'),(31,'Can delete device',8,'delete_device'),(32,'Can view device',8,'view_device'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add log',10,'add_log'),(38,'Can change log',10,'change_log'),(39,'Can delete log',10,'delete_log'),(40,'Can view log',10,'view_log'),(41,'Can add gate',11,'add_gate'),(42,'Can change gate',11,'change_gate'),(43,'Can delete gate',11,'delete_gate'),(44,'Can view gate',11,'view_gate');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'gatechecker','building'),(8,'gatechecker','device'),(11,'gatechecker','gate'),(10,'gatechecker','log'),(9,'gatechecker','user'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-09-01 21:56:13.517221'),(2,'auth','0001_initial','2021-09-01 21:56:13.652182'),(3,'admin','0001_initial','2021-09-01 21:56:13.889829'),(4,'admin','0002_logentry_remove_auto_add','2021-09-01 21:56:13.941566'),(5,'admin','0003_logentry_add_action_flag_choices','2021-09-01 21:56:13.951767'),(6,'contenttypes','0002_remove_content_type_name','2021-09-01 21:56:14.008986'),(7,'auth','0002_alter_permission_name_max_length','2021-09-01 21:56:14.031317'),(8,'auth','0003_alter_user_email_max_length','2021-09-01 21:56:14.062672'),(9,'auth','0004_alter_user_username_opts','2021-09-01 21:56:14.075247'),(10,'auth','0005_alter_user_last_login_null','2021-09-01 21:56:14.109783'),(11,'auth','0006_require_contenttypes_0002','2021-09-01 21:56:14.112053'),(12,'auth','0007_alter_validators_add_error_messages','2021-09-01 21:56:14.123861'),(13,'auth','0008_alter_user_username_max_length','2021-09-01 21:56:14.153018'),(14,'auth','0009_alter_user_last_name_max_length','2021-09-01 21:56:14.182386'),(15,'auth','0010_alter_group_name_max_length','2021-09-01 21:56:14.207659'),(16,'auth','0011_update_proxy_permissions','2021-09-01 21:56:14.217360'),(17,'gatechecker','0001_initial','2021-09-01 21:56:14.356728'),(18,'sessions','0001_initial','2021-09-01 21:56:14.431386'),(19,'gatechecker','0002_auto_20210904_0952','2021-09-04 09:52:11.779269');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gatechecker_building`
--

DROP TABLE IF EXISTS `gatechecker_building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gatechecker_building` (
  `building_id` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `location` longtext NOT NULL,
  `to_user_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`building_id`),
  KEY `gatechecker_building_to_user_id_157dafcb_fk_gatecheck` (`to_user_id`),
  CONSTRAINT `gatechecker_building_to_user_id_157dafcb_fk_gatecheck` FOREIGN KEY (`to_user_id`) REFERENCES `gatechecker_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gatechecker_building`
--

LOCK TABLES `gatechecker_building` WRITE;
/*!40000 ALTER TABLE `gatechecker_building` DISABLE KEYS */;
INSERT INTO `gatechecker_building` VALUES ('B1','sky tree','Tokyo','U1'),('B2','iias','Tsukuba','U1'),('B3','AEON Mall','Tsuchiura','U2'),('B4','Wing','Hitachinaka','U2'),('B5','Cross Hotel','Sapporo','U3');
/*!40000 ALTER TABLE `gatechecker_building` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gatechecker_device`
--

DROP TABLE IF EXISTS `gatechecker_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gatechecker_device` (
  `device_id` varchar(20) NOT NULL,
  `is_entrance` tinyint(1) NOT NULL,
  `is_using` tinyint(1) NOT NULL,
  `last_alert_time` datetime(6) NOT NULL,
  `to_gate_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`device_id`),
  KEY `gatechecker_device_to_gate_id_4b2f8071_fk_gatecheck` (`to_gate_id`),
  CONSTRAINT `gatechecker_device_to_gate_id_4b2f8071_fk_gatecheck` FOREIGN KEY (`to_gate_id`) REFERENCES `gatechecker_gate` (`gate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gatechecker_device`
--

LOCK TABLES `gatechecker_device` WRITE;
/*!40000 ALTER TABLE `gatechecker_device` DISABLE KEYS */;
INSERT INTO `gatechecker_device` VALUES ('D1',1,1,'2020-10-10 10:10:10.000000','G1'),('D2',0,1,'2020-10-10 10:10:10.000000','G1'),('D3',1,1,'2020-10-10 10:10:10.000000','G3'),('D4',0,1,'2020-10-10 10:10:10.000000','G4'),('D5',1,1,'2020-10-10 10:10:10.000000','G5');
/*!40000 ALTER TABLE `gatechecker_device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gatechecker_gate`
--

DROP TABLE IF EXISTS `gatechecker_gate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gatechecker_gate` (
  `gate_id` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `is_open` tinyint(1) NOT NULL,
  `to_building_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`gate_id`),
  KEY `gatechecker_gate_to_building_id_74460662_fk_gatecheck` (`to_building_id`),
  CONSTRAINT `gatechecker_gate_to_building_id_74460662_fk_gatecheck` FOREIGN KEY (`to_building_id`) REFERENCES `gatechecker_building` (`building_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gatechecker_gate`
--

LOCK TABLES `gatechecker_gate` WRITE;
/*!40000 ALTER TABLE `gatechecker_gate` DISABLE KEYS */;
INSERT INTO `gatechecker_gate` VALUES ('G1','正門',1,'B1'),('G2','東門',0,'B2'),('G3','西門',1,'B2'),('G4','南門',1,'B2'),('G5','正門',1,'B3'),('G6','正門',1,'B4'),('G7','正門',1,'B5'),('G8','裏門',0,'B5');
/*!40000 ALTER TABLE `gatechecker_gate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gatechecker_log`
--

DROP TABLE IF EXISTS `gatechecker_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gatechecker_log` (
  `log_id` varchar(20) NOT NULL,
  `temperature` double NOT NULL,
  `time` datetime(6) NOT NULL,
  `is_blacklist` tinyint(1) NOT NULL,
  `to_device_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `gatechecker_log_to_device_id_17767803_fk_gatecheck` (`to_device_id`),
  CONSTRAINT `gatechecker_log_to_device_id_17767803_fk_gatecheck` FOREIGN KEY (`to_device_id`) REFERENCES `gatechecker_device` (`device_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gatechecker_log`
--

LOCK TABLES `gatechecker_log` WRITE;
/*!40000 ALTER TABLE `gatechecker_log` DISABLE KEYS */;
INSERT INTO `gatechecker_log` VALUES ('L001',35.8,'2021-09-01 19:34:10.000000',1,'D1'),('L002',37.1,'2021-09-01 19:36:23.000000',0,'D1'),('L003',35.7,'2021-09-01 19:48:23.000000',1,'D2'),('L004',36.3,'2021-09-01 19:51:47.000000',0,'D2'),('L005',37.9,'2021-09-01 19:51:49.000000',0,'D3'),('L006',37.3,'2021-09-01 20:11:30.000000',0,'D1'),('L007',36.4,'2021-09-01 21:23:40.000000',1,'D5');
/*!40000 ALTER TABLE `gatechecker_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gatechecker_user`
--

DROP TABLE IF EXISTS `gatechecker_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gatechecker_user` (
  `user_id` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gatechecker_user`
--

LOCK TABLES `gatechecker_user` WRITE;
/*!40000 ALTER TABLE `gatechecker_user` DISABLE KEYS */;
INSERT INTO `gatechecker_user` VALUES ('U1','三井不動産'),('U2','Yahoo不動産'),('U3','北海道不動産'),('U4','東横イン'),('U5','野村不動産'),('U6','セキスイハイム'),('U7','飯田ホールディングス'),('U8','住友林業'),('U9','ヘーベルハウス');
/*!40000 ALTER TABLE `gatechecker_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-14 22:34:51
