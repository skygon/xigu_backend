-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: xigu_backend
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 产品描述',7,'add_projectdescription'),(20,'Can change 产品描述',7,'change_projectdescription'),(21,'Can delete 产品描述',7,'delete_projectdescription'),(22,'Can add 产品',8,'add_project'),(23,'Can change 产品',8,'change_project'),(24,'Can delete 产品',8,'delete_project'),(25,'Can add 图片',9,'add_image'),(26,'Can change 图片',9,'change_image'),(27,'Can delete 图片',9,'delete_image'),(28,'Can add 基金类产品',10,'add_fund'),(29,'Can change 基金类产品',10,'change_fund'),(30,'Can delete 基金类产品',10,'delete_fund'),(31,'Can add 基金类产品',11,'add_insurance'),(32,'Can change 基金类产品',11,'change_insurance'),(33,'Can delete 基金类产品',11,'delete_insurance'),(34,'Can add real estate',12,'add_realestate'),(35,'Can change real estate',12,'change_realestate'),(36,'Can delete real estate',12,'delete_realestate'),(37,'Can add 商业地产类产品',13,'add_commercialestate'),(38,'Can change 商业地产类产品',13,'change_commercialestate'),(39,'Can delete 商业地产类产品',13,'delete_commercialestate'),(40,'Can add 用户表',14,'add_user'),(41,'Can change 用户表',14,'change_user'),(42,'Can delete 用户表',14,'delete_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$Qe9RxRyLJRHV$1YZHv8TMxPs6aOsyfnPLLFLklo7dWqIkle1KX2BVgIA=','2018-08-08 07:54:08.853831',1,'admin','','','admin@123.com',1,1,'2018-08-08 05:43:15.044656');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `commercial_estate`
--

LOCK TABLES `commercial_estate` WRITE;
/*!40000 ALTER TABLE `commercial_estate` DISABLE KEYS */;
INSERT INTO `commercial_estate` VALUES (1,'堪萨斯城房产项目','8-10%','1200万美金','5万美金','3年');
/*!40000 ALTER TABLE `commercial_estate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-08-08 08:00:35.845823','1','柯罗尼CIF物流地产基金',1,'[{\"added\": {}}]',7,1),(2,'2018-08-08 08:00:38.313809','1','柯罗尼CIF物流地产基金',1,'[{\"added\": {}}]',8,1),(3,'2018-08-08 08:13:29.304148','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',7,1),(4,'2018-08-08 08:26:24.450484','2','克罗尼-pdf',1,'[{\"added\": {}}]',7,1),(5,'2018-08-08 08:26:36.348878','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"project_detail\"]}}]',8,1),(6,'2018-08-08 08:30:00.196791','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"project_detail\"]}}]',8,1),(7,'2018-08-08 08:34:04.714096','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"content\"]}}]',7,1),(8,'2018-08-09 03:32:52.468944','1','柯罗尼CIF物流地产基金',1,'[{\"added\": {}}]',10,1),(9,'2018-08-09 03:32:54.494263','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"fund\"]}}]',8,1),(10,'2018-08-09 03:38:23.915077','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"fund\"]}}]',8,1),(11,'2018-08-09 03:39:12.247600','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"fund\"]}}]',8,1),(12,'2018-08-09 08:32:40.117638','3','特级「隽升」储蓄保障计划 II',1,'[{\"added\": {}}]',7,1),(13,'2018-08-09 08:32:44.283946','1','特级「隽升」储蓄保障计划 II',1,'[{\"added\": {}}]',11,1),(14,'2018-08-09 08:32:47.953295','2','特级「隽升」储蓄保障计划 II',1,'[{\"added\": {}}]',8,1),(15,'2018-08-09 09:09:02.839471','1','柯罗尼CIF物流地产基金',2,'[{\"changed\": {\"fields\": [\"project_detail\"]}}]',8,1),(16,'2018-08-09 09:09:09.103248','2','特级「隽升」储蓄保障计划 II',2,'[{\"changed\": {\"fields\": [\"project_detail\"]}}]',8,1),(17,'2018-08-09 11:22:12.985704','1','奥兰多魔幻·度假庄园三期',1,'[{\"added\": {}}]',12,1),(18,'2018-08-09 11:22:35.199942','4','奥兰多魔幻·度假庄园三期',1,'[{\"added\": {}}]',7,1),(19,'2018-08-09 11:22:39.672921','3','奥兰多魔幻·度假庄园三期',1,'[{\"added\": {}}]',8,1),(20,'2018-08-10 01:59:04.043482','1','堪萨斯城房产项目',1,'[{\"added\": {}}]',13,1),(21,'2018-08-10 01:59:35.881106','5','堪萨斯城房产项目',1,'[{\"added\": {}}]',7,1),(22,'2018-08-10 01:59:38.349182','4','堪萨斯城房产项目',1,'[{\"added\": {}}]',8,1),(23,'2018-08-10 03:41:35.527640','1','特级「隽升」储蓄保障计划 II',2,'[{\"changed\": {\"fields\": [\"age_range\"]}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(4,'auth','permission'),(2,'auth','user'),(5,'contenttypes','contenttype'),(13,'project','commercialestate'),(10,'project','fund'),(9,'project','image'),(11,'project','insurance'),(8,'project','project'),(7,'project','projectdescription'),(12,'project','realestate'),(6,'sessions','session'),(14,'user_manage','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-08-08 05:34:01.572131'),(2,'auth','0001_initial','2018-08-08 05:34:02.258784'),(3,'admin','0001_initial','2018-08-08 05:34:02.429965'),(4,'admin','0002_logentry_remove_auto_add','2018-08-08 05:34:02.459329'),(5,'contenttypes','0002_remove_content_type_name','2018-08-08 05:34:02.558403'),(6,'auth','0002_alter_permission_name_max_length','2018-08-08 05:34:02.627474'),(7,'auth','0003_alter_user_email_max_length','2018-08-08 05:34:02.684243'),(8,'auth','0004_alter_user_username_opts','2018-08-08 05:34:02.701268'),(9,'auth','0005_alter_user_last_login_null','2018-08-08 05:34:02.744194'),(10,'auth','0006_require_contenttypes_0002','2018-08-08 05:34:02.748476'),(11,'auth','0007_alter_validators_add_error_messages','2018-08-08 05:34:02.762097'),(12,'auth','0008_alter_user_username_max_length','2018-08-08 05:34:02.882599'),(13,'auth','0009_alter_user_last_name_max_length','2018-08-08 05:34:02.962396'),(14,'project','0001_initial','2018-08-08 05:34:03.186301'),(15,'sessions','0001_initial','2018-08-08 05:34:03.251001'),(16,'project','0002_project_tags','2018-08-08 07:55:59.755664'),(17,'project','0003_auto_20180809_0328','2018-08-09 03:29:04.545117'),(18,'project','0004_auto_20180809_0829','2018-08-09 08:29:18.899163'),(19,'project','0005_auto_20180809_0906','2018-08-09 09:06:27.687567'),(20,'project','0006_auto_20180809_1014','2018-08-09 10:15:01.813237'),(21,'project','0007_project_commercial_estate','2018-08-09 10:52:15.683801'),(22,'project','0008_auto_20180810_0341','2018-08-10 03:41:16.644488'),(23,'user_manage','0001_initial','2018-08-10 05:49:27.129219');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1tln8e8l5k4tkq52f97b7vi37pkf9p07','OTRiYmQyOGY0MDMzMDQzZjg0MzkxNDVkMjlhNzc4NzllZWNkYzhjMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkNTU1MmQ3ZDc1YzQxNjZlMDg3NjM1M2JkNWFkZTI2M2U1NzVjOWUyIn0=','2018-08-22 07:54:08.857897'),('mrmc2oi2zplvunbsamf6vtuq9fkguh0j','YWU4ODRmNWZjNzdkMDQxNmJhMWNiOWY5MTlhMTRkYjFkOWJlOWU4Zjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiJkNTU1MmQ3ZDc1YzQxNjZlMDg3NjM1M2JkNWFkZTI2M2U1NzVjOWUyIn0=','2018-08-22 05:43:25.916768');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `fund`
--

LOCK TABLES `fund` WRITE;
/*!40000 ALTER TABLE `fund` DISABLE KEYS */;
INSERT INTO `fund` VALUES (1,'柯罗尼CIF物流地产基金','8-10%',NULL,'5.6%','30万美金','5万美金','1+1+1年');
/*!40000 ALTER TABLE `fund` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `insurance`
--

LOCK TABLES `insurance` WRITE;
/*!40000 ALTER TABLE `insurance` DISABLE KEYS */;
INSERT INTO `insurance` VALUES (1,'特级「隽升」储蓄保障计划 II','6.56%','2万美金','1//5/8/12年','1-75周岁');
/*!40000 ALTER TABLE `insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'柯罗尼CIF物流地产基金',1,1,1,0,'稳定分红#资产增值#风险分散',1,NULL,1,NULL,NULL),(2,'特级「隽升」储蓄保障计划 II',2,1,1,0,'长线储蓄#随时更换受保人',NULL,1,3,NULL,NULL),(3,'奥兰多魔幻·度假庄园三期',2,1,1,0,'高收益率#稀缺地段#顶尖设计',NULL,NULL,4,1,NULL),(4,'堪萨斯城房产项目',3,1,1,0,'5万美金起投#年化8-10%#包租收益',NULL,NULL,5,NULL,1);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `project_desc`
--

LOCK TABLES `project_desc` WRITE;
/*!40000 ALTER TABLE `project_desc` DISABLE KEYS */;
INSERT INTO `project_desc` VALUES (1,'柯罗尼CIF物流地产基金','<p style=\"text-align: center;\"><img src=\"http://img.fang88.com/ng_server_upload/0006_20180808081153_494.jpg\" style=\"width: 1335px; height: 1088px;\" width=\"1335\" height=\"1088\"/></p><p><br/></p><p><br/></p><p style=\"text-align: center;\"><img src=\"http://img.fang88.com/ng_server_upload/0005_20180808081153_642.jpg\" width=\"1335\" height=\"1080\"/></p><p><br/></p><p></p><p><br/></p>'),(2,'克罗尼-pdf','<p style=\"line-height: 16px;\"><img style=\"vertical-align: middle; margin-right: 2px;\" src=\"http://192.168.0.106:8000/static/ueditor/dialogs/attachment/fileTypeImages/icon_pdf.gif\"/><a style=\"font-size:12px; color:#0066cc;\" href=\"/upload/东南亚消费分期固定收益基金1807_20180808082600_446.pdf\" title=\"东南亚消费分期固定收益基金1807.pdf\">东南亚消费分期固定收益基金1807.pdf</a></p><p><br/></p>'),(3,'特级「隽升」储蓄保障计划 II','<p><span data-shimo-docs=\"[[20,&quot;产品信息】\\n保诚保险：&quot;],[20,&quot;\\n&quot;,&quot;list-start:\\&quot;1\\&quot;|ordered:\\&quot;decimal\\&quot;&quot;],[20,&quot;产品名称：特级「隽升」储蓄保障计划 II&quot;],[20,&quot;\\n&quot;,&quot;bullet-id:\\&quot;TQ0P\\&quot;|bullet:\\&quot;circle\\&quot;&quot;],[20,&quot;产品特点：长线储蓄，保单没有潜在红利；预计年回报率不低于6.5%；最高贷款额为保单现金价值的80%；可随时更换受保人。&quot;],[20,&quot;预期年化回报率：6.58%&quot;,&quot;1:\\&quot;%23f9eda6\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;bullet-id:\\&quot;TQ0P\\&quot;|bullet:\\&quot;circle\\&quot;&quot;],[20,&quot;产品说明：&quot;],[20,&quot;\\n&quot;,&quot;bullet-id:\\&quot;TQ0P\\&quot;|bullet:\\&quot;circle\\&quot;&quot;]]\"></span></p><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">产品信息】</span></p><ol data-list-style=\"decimal\" class=\"ql-long-9242890 list-paddingleft-2\"><li><p><span class=\"ql-author-9242890\">保诚保险：</span></p></li></ol><ul data-list-style=\"circle\" class=\"ql-long-9242890 list-paddingleft-2\"><li><p><span class=\"ql-author-9242890\">产品名称：特级「隽升」储蓄保障计划 II</span></p></li></ul><ul data-list-style=\"circle\" class=\"ql-long-9242890 list-paddingleft-2\"><li><p><span class=\"ql-author-9242890\">产品特点：长线储蓄，保单没有潜在红利；预计年回报率不低于6.5%；最高贷款额为保单现金价值的80%；可随时更换受保人。</span><span class=\"ql-author-9242890\" style=\"background-color: rgb(249, 237, 166);\">预期年</span><span style=\"background-color: rgb(249, 237, 166);\" class=\"ql-author-7540409\">化</span><span class=\"ql-author-9242890\" style=\"background-color: rgb(249, 237, 166);\">回报</span><span style=\"background-color: rgb(249, 237, 166);\" class=\"ql-author-7540409\">率</span><span class=\"ql-author-9242890\" style=\"background-color: rgb(249, 237, 166);\">：6.58%</span></p></li></ul><ul data-list-style=\"circle\" class=\"ql-long-9242890 list-paddingleft-2\"><li><p><span class=\"ql-author-9242890\">产品说明：</span></p></li></ul><span data-shimo-docs=\"[[30,[{&quot;A1&quot;:[40,[[20,&quot;投保年龄&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B1&quot;:[40,[[20,&quot;1-75岁&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;A2&quot;:[40,[[20,&quot;缴费期限&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B2&quot;:[40,[[20,&quot;1年，5年，8年，12年&quot;,&quot;1:\\&quot;%23f9eda6\\&quot;|26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;&quot;]]],&quot;A3&quot;:[40,[[20,&quot;交费方式&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B3&quot;:[40,[[20,&quot;港元／人民幣／美元 按年缴费&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;A4&quot;:[40,[[20,&quot;投资门槛&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B4&quot;:[40,[[20,&quot;2万美金起投&quot;,&quot;1:\\&quot;%23f9eda6\\&quot;|26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;&quot;]]],&quot;A5&quot;:[40,[[20,&quot;分红期限&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B5&quot;:[40,[[20,&quot;全部取出/投保人到100岁/投保人身故&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;A6&quot;:[40,[[20,&quot;人寿保障&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B6&quot;:[40,[[20,&quot;若受保人不幸身故，已缴总保费加2500美金/20000港币，或者保单现金价值&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;A7&quot;:[40,[[20,&quot;保单贷款&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B7&quot;:[40,[[20,&quot;现金价值80%的款项可用来贷款&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]]},[[10,7]],[[10,1,&quot;3:137&quot;],[10,1,&quot;3:479&quot;]]],&quot;25:\\&quot;x1nGvG\\&quot;&quot;]]\"><table width=\"568\"><tbody><tr class=\"firstRow\" height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"48\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">投保年龄</span></p></td><td class=\"ql-sheet-cell selected\" width=\"152\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">1-75岁</span></p></td></tr><tr height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"48\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">缴费期限</span></p></td><td class=\"ql-sheet-cell selected\" width=\"152\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\" style=\"background-color: rgb(249, 237, 166);\">1年，5年，8年，12年</span></p></td></tr><tr height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"48\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">交费方式</span></p></td><td class=\"ql-sheet-cell selected\" width=\"152\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">港元／人民幣／美元 按年缴费</span></p></td></tr><tr height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"48\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">投资门槛</span></p></td><td class=\"ql-sheet-cell selected\" width=\"152\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\" style=\"background-color: rgb(249, 237, 166);\">2万美金起投</span></p></td></tr><tr height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"48\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">分红期限</span></p></td><td class=\"ql-sheet-cell selected\" style=\"word-break: break-all;\" width=\"152\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">全部取出/投保人到100岁/投保人身故</span></p></td></tr><tr height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"48\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">人寿保障</span></p></td><td class=\"ql-sheet-cell selected\" width=\"152\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">若受保人不幸身故，已缴总保费加2500美金/20000港币，或者保单现金价值</span></p></td></tr><tr height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"48\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">保单贷款</span></p></td><td class=\"ql-sheet-cell selected\" width=\"152\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">现金价值80%的款项可用来贷款</span></p></td></tr></tbody></table></span><p></p><p><br/></p><p><span data-shimo-docs=\"[[20,&quot;案例分析：\\n郑女士为刚出生的女儿买了保险，每年投资10万美金，储蓄5年，总投资50万美金&quot;]]\"></span></p><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">案例分析：</span></p><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">郑女士为刚出生的女儿买了保险，每年投资10万美金，储蓄5年，总投资50万美金</span></p><span data-shimo-docs=\"[[30,[{&quot;A1&quot;:[40,[[20,&quot;0岁&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B1&quot;:[40,[[20,&quot;18-22岁&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;C1&quot;:[40,[[20,&quot;30岁&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;D1&quot;:[40,[[20,&quot;55岁&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;E1&quot;:[40,[[20,&quot;传承&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;A2&quot;:[40,[[20,&quot;每年投资10万，5年总投资50万美金&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;B2&quot;:[40,[[20,&quot;每年提取10万美金作为助学金，4年共计40万美金&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;C2&quot;:[40,[[20,&quot;结婚置业，可一次性提出100万美金用于结婚，创业&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;D2&quot;:[40,[[20,&quot;退休养老，每年可提取25万美金，安心享受退休养老生活&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]],&quot;E2&quot;:[40,[[20,&quot;100岁时，账户余额5000多万美元，可传承给下一代。&quot;,&quot;26:\\&quot;9242890\\&quot;&quot;],[20,&quot;\\n&quot;,&quot;24:\\&quot;init\\&quot;|26:\\&quot;9242890\\&quot;&quot;]]]},[[10,2]],[[10,1,&quot;3:115&quot;],[10,1,&quot;3:128&quot;],[10,1,&quot;3:131&quot;],[10,1,&quot;3:122&quot;],[10,1,&quot;3:119&quot;]]],&quot;25:\\&quot;sqr3Zm\\&quot;&quot;]]\"><table width=\"568\"><tbody><tr class=\"firstRow\" height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"38\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">0岁</span></p></td><td class=\"ql-sheet-cell selected\" width=\"42\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">18-22岁</span></p></td><td class=\"ql-sheet-cell selected\" width=\"41\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">30岁</span></p></td><td class=\"ql-sheet-cell selected\" width=\"39\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">55岁</span></p></td><td class=\"ql-sheet-cell selected\" width=\"39\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">传承</span></p></td></tr><tr height=\"undefined\"><td class=\"ql-sheet-cell selected\" width=\"38\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">每年投资10万，5年总投资50万美金</span></p></td><td class=\"ql-sheet-cell selected\" width=\"42\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">每年提取10万美金作为助学金，4年共计40万美金</span></p></td><td class=\"ql-sheet-cell selected\" width=\"41\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">结婚置业，可一次性提出100万美金用于结婚，创业</span></p></td><td class=\"ql-sheet-cell selected\" width=\"39\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">退休养老，每年可提取25万美金，安心享受退休养老生活</span></p></td><td class=\"ql-sheet-cell selected\" width=\"39\" contenteditable=\"true\"><p><span class=\"ql-author-9242890\">100岁时，账户余额5000多万美元，可传承给下一代。</span></p></td></tr></tbody></table></span><p></p><p><span data-shimo-docs=\"[[20,&quot;公司介绍：&quot;]]\">公司介绍：</span></p><p><img class=\"gallery-image\" data-src=\"https://p3.pstatp.com/large/pgc-image/15228264081019e608dc49a\" alt=\"\" data-width=\"612px\" data-height=\"458.031px\" data-layout=\"embed\" data-author=\"9242890\" data-margin=\"none\" data-crop=\"\" style=\"margin: initial; transform: initial; max-width: 100%;\" data-frame=\"none\" data-ori-height=\"458\" data-ori-width=\"612\" src=\"https://p3.pstatp.com/large/pgc-image/15228264081019e608dc49a\" width=\"612px\" height=\"458.031px\"/></p>'),(4,'奥兰多魔幻·度假庄园三期','<p><span data-shimo-docs=\"[[20,&quot;奥兰多MV项目\\n奥兰多魔幻·度假庄园三期\\n年化回报率：\\n12.70%\\n起投金额：52万美元，首付仅2成\\n物业类型：联排别墅\\n户型：三房-269.48 ㎡，四房-284.59 ㎡\\n交房日期：2020年\\n\\n&quot;],[20,&quot;高收益率&quot;,&quot;0:\\&quot;%2379c6cd\\&quot;&quot;],[20,&quot;\\n&quot;],[20,&quot;稀缺地段&quot;,&quot;0:\\&quot;%2379c6cd\\&quot;&quot;],[20,&quot;\\n&quot;],[20,&quot;顶尖设计&quot;,&quot;0:\\&quot;%2379c6cd\\&quot;&quot;],[20,&quot;\\n&quot;],[20,&quot;极致湖景&quot;,&quot;0:\\&quot;%2379c6cd\\&quot;&quot;],[20,&quot;\\n&quot;],[20,&quot;豪华装修&quot;,&quot;0:\\&quot;%2379c6cd\\&quot;&quot;],[20,&quot;\\n\\n专家点评\\n1.奥兰多位于美国佛罗里达州的中部地区，被称为“美国度假之都”，拥有包括华特·迪士尼乐园、环球影城等在内的五大亲子乐园，两千米海岸线，项目处于稀缺地段，位于192公路，毗邻迪士尼王国，车程5-15分钟。奥兰多游客量7200万，预计缺口184000间客房，有实际的客房需求。&nbsp;已经运营的Magic Village一期度假屋收益稳定，常年入住率高于70%，年净租金收益率达到9.3%。2. 美国地产市场前景可观，美国地产仍处于投资上升期，项目同邮编地区挂牌中位数为359,945美元，所在地区的Median Sales/List 98%，预测未来一年34747地区房价将上涨5%&nbsp;。3.该地区失业率仅3.6%，低于美国平均失业率；家庭年收入75000美元，高于州平均收入；治安良好。4.经验丰富的合作方：开发商Magic是美国佛州高端房产开发领域的翘楚。 \\n\\n开发商介绍\\n梦幻度假集团是佛州第四大开发商，拥有10年房产开发及管理经验，销售总金额已经超过35亿美金！拥有市区多处办公楼物业，目前专注度假别墅、分时度假酒店及商办综合体开发，定位为高端奢华的假期体验。旗下项目包括：法拉利设计公司·宾尼法利纳设计的商办综合体-Magic place、高端酒店式公寓-Magic reserve、高端度假别墅Magic village1 / 2 / 3 ，并同多方强强合作，给业主带来高端且放心的体验：专注度假房屋的CND管理公司在业主不在的时候代为管理房屋并提供出租机会；【第三家园计划】隶属全球高端私人俱乐部，我公司业主可加入享受全球豪宅兑换居住特权；鼎信管理公司专门为开发商Magic提供完整定制的酒店管理顾问服务；世界最大独立酒店品牌，在85个国家里拥有650个独特的物业。借助这样的合作，开发商Magic的项目将通过品牌声誉、全球分销、销售及市场整合方案而具有战略优势，所有的客人都有资格进入并享用iPrefer酒店奖励计划。&quot;]]\"><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">奥兰多MV项目</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">奥兰多魔幻·度假庄园三期</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">年化回报率：</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">12.70%</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">起投金额：52万美元，首付仅2成</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">物业类型：联排别墅</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">户型：三房-269.48 ㎡，四房-284.59 ㎡</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">交房日期：2020年</span></p><p><br/></p><p class=\"ql-long-13492647\"><span style=\"color: rgb(121, 198, 205);\" class=\"ql-author-13492647\">高收益率</span></p><p class=\"ql-long-13492647\"><span style=\"color: rgb(121, 198, 205);\" class=\"ql-author-13492647\">稀缺地段</span></p><p class=\"ql-long-13492647\"><span style=\"color: rgb(121, 198, 205);\" class=\"ql-author-13492647\">顶尖设计</span></p><p class=\"ql-long-13492647\"><span style=\"color: rgb(121, 198, 205);\" class=\"ql-author-13492647\">极致湖景</span></p><p class=\"ql-long-13492647\"><span style=\"color: rgb(121, 198, 205);\" class=\"ql-author-13492647\">豪华装修</span></p><p><br/></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">专家点评</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">1.奥兰多位于美国佛罗里达州的中部地区，被称为“美国度假之都”，拥有包括华特·迪士尼乐园、环球影城等在内的五大亲子乐园，两千米海岸线，项目处于稀缺地段，位于192公路，毗邻迪士尼王国，车程5-15分钟。奥兰多游客量7200万，预计缺口184000间客房，有实际的客房需求。&nbsp;已经运营的Magic Village一期度假屋收益稳定，常年入住率高于70%，年净租金收益率达到9.3%。2. 美国地产市场前景可观，美国地产仍处于投资上升期，项目同邮编地区挂牌中位数为359,945美元，所在地区的Median Sales/List 98%，预测未来一年34747地区房价将上涨5%&nbsp;。3.该地区失业率仅3.6%，低于美国平均失业率；家庭年收入75000美元，高于州平均收入；治安良好。4.经验丰富的合作方：开发商Magic是美国佛州高端房产开发领域的翘楚。 </span></p><p><br/></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">开发商介绍</span></p><p class=\"ql-long-13492647\"><span class=\"ql-author-13492647\">梦幻度假集团是佛州第四大开发商，拥有10年房产开发及管理经验，销售总金额已经超过35亿美金！拥有市区多处办公楼物业，目前专注度假别墅、分时度假酒店及商办综合体开发，定位为高端奢华的假期体验。旗下项目包括：法拉利设计公司·宾尼法利纳设计的商办综合体-Magic place、高端酒店式公寓-Magic reserve、高端度假别墅Magic village1 / 2 / 3 ，并同多方强强合作，给业主带来高端且放心的体验：专注度假房屋的CND管理公司在业主不在的时候代为管理房屋并提供出租机会；【第三家园计划】隶属全球高端私人俱乐部，我公司业主可加入享受全球豪宅兑换居住特权；鼎信管理公司专门为开发商Magic提供完整定制的酒店管理顾问服务；世界最大独立酒店品牌，在85个国家里拥有650个独特的物业。借助这样的合作，开发商Magic的项目将通过品牌声誉、全球分销、销售及市场整合方案而具有战略优势，所有的客人都有资格进入并享用iPrefer酒店奖励计划。</span></p></span></p>'),(5,'堪萨斯城房产项目','<p><span data-shimo-docs=\"[[20,&quot;-堪萨斯城房产项目：永久产权  5万美金起投  年华8%-10%包租收益\\n特点：高回报，稳定收益，总投入低\\n\\n开发商介绍：\\n\\n产品介绍：\\n-特色：独栋别墅，永久产权，现房，3-5天过户，同月产生收益，2年包租，包维修，保证8%年净收益。&quot;]]\"><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">-堪萨斯城房产项目：永久产权 &nbsp;5万美金起投 &nbsp;年华8%-10%包租收益</span></p><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">特点：高回报，稳定收益，总投入低</span></p><p><br/></p><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">开发商介绍：</span></p><p><br/></p><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">产品介绍：</span></p><p class=\"ql-long-9242890\"><span class=\"ql-author-9242890\">-特色：独栋别墅，永久产权，现房，3-5天过户，同月产生收益，2年包租，包维修，保证8%年净收益。</span></p></span></p>');
/*!40000 ALTER TABLE `project_desc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `real_estate`
--

LOCK TABLES `real_estate` WRITE;
/*!40000 ALTER TABLE `real_estate` DISABLE KEYS */;
INSERT INTO `real_estate` VALUES (1,'奥兰多魔幻·度假庄园三期','12.70%','townhouse','4','126平米');
/*!40000 ALTER TABLE `real_estate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_follow_projects`
--

LOCK TABLES `user_follow_projects` WRITE;
/*!40000 ALTER TABLE `user_follow_projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_follow_projects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-13 11:45:11
