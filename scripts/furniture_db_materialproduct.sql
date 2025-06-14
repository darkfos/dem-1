-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: furniture_db
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `materialproduct`
--

DROP TABLE IF EXISTS `materialproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialproduct` (
  `id_material_product` int NOT NULL AUTO_INCREMENT,
  `id_material` int DEFAULT NULL,
  `id_product` int DEFAULT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`id_material_product`),
  KEY `id_material` (`id_material`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `materialproduct_ibfk_1` FOREIGN KEY (`id_material`) REFERENCES `material` (`id_material`),
  CONSTRAINT `materialproduct_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `product` (`id_product`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialproduct`
--

LOCK TABLES `materialproduct` WRITE;
/*!40000 ALTER TABLE `materialproduct` DISABLE KEYS */;
INSERT INTO `materialproduct` VALUES (1,4,1,1),(2,10,1,2),(3,11,1,2),(4,12,1,2),(5,14,1,1),(6,16,1,5),(7,17,1,1),(8,18,1,1),(9,19,1,1),(10,4,2,1),(11,9,2,3),(12,11,2,2),(13,12,2,3),(14,14,2,1),(15,16,2,5),(16,17,2,1),(17,18,2,1),(18,19,2,1),(19,4,3,2),(20,9,3,4),(21,10,3,2),(22,14,3,1),(23,16,3,5),(24,17,3,1),(25,18,3,1),(26,19,3,1),(27,5,4,3),(28,20,4,6),(29,2,5,3),(30,3,5,2),(31,6,5,3),(32,8,5,2),(33,2,6,2),(34,3,6,2),(35,8,6,2),(36,5,7,2),(37,20,7,7),(38,6,8,6),(39,15,8,1),(40,5,9,4),(41,20,9,9),(42,6,10,8),(43,8,10,1),(44,15,10,1),(45,5,11,6),(46,20,11,6),(47,4,12,3),(48,5,12,5),(49,5,12,5),(50,20,12,9),(51,1,13,4),(52,3,13,2),(53,8,13,2),(54,1,14,8),(55,3,14,7),(56,5,14,5),(57,6,14,6),(58,8,14,2),(59,9,14,2),(60,5,15,4),(61,16,15,4),(62,20,15,7),(63,2,16,0),(64,16,16,4),(65,3,17,1),(66,5,17,8),(67,20,17,6),(68,3,18,3),(69,4,18,4),(70,3,19,1),(71,5,19,8),(72,8,19,1),(73,1,20,2),(74,3,20,4),(75,8,20,2);
/*!40000 ALTER TABLE `materialproduct` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-14 16:34:30
