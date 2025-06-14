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
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material` (
  `id_material` int NOT NULL AUTO_INCREMENT,
  `name_material` varchar(255) DEFAULT NULL,
  `id_type_material` int DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `min_quantity` int DEFAULT NULL,
  `quanity_in_yp` int DEFAULT NULL,
  `ed` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_material`),
  KEY `id_type_material` (`id_type_material`),
  CONSTRAINT `material_ibfk_1` FOREIGN KEY (`id_type_material`) REFERENCES `materialtype` (`id_type_material`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
INSERT INTO `material` VALUES (1,'Цельный массив дерева Дуб 1000х600 мм',1,7450.00,1500,500,7,'м²'),(2,'Клееный массив дерева Дуб 1000х600 мм',1,4520.00,300,500,7,'м²'),(3,'Шпон облицовочный Дуб натуральный 2750х480 мм',1,2500.00,2000,1500,20,'м²'),(4,'Фанера 2200х1000 мм',2,2245.00,450,1000,53,'м²'),(5,'ДСП 2750х1830 мм',2,529.60,1010,1200,181,'м²'),(6,'МДФ 2070х1400 мм',2,417.24,1550,1000,87,'м²'),(7,'ДВП 2440х2050 мм',2,187.00,1310,1000,190,'м²'),(8,'ХДФ 2800x2070 мм',2,370.96,1400,1200,90,'м²'),(9,'Экокожа 140 см',3,1600.00,1200,1500,100,'пог.м'),(10,'Велюр 140 см',3,1300.00,1300,1500,100,'пог.м'),(11,'Шенилл 140 см',3,620.00,950,1500,100,'пог.м'),(12,'Рогожка 140 см',3,720.00,960,1500,100,'пог.м'),(13,'Закаленное стекло 2600х1800 мм',4,1148.00,1000,500,197,'м²'),(14,'Металлокаркас для стула',5,1100.00,300,250,5,'шт'),(15,'Металлокаркас каркас из профиля с траверсами для стола',5,6700.00,100,100,1,'шт'),(16,'Колесо для мебели поворотное',6,10.59,1500,1000,500,'шт'),(17,'Газ-лифт',5,730.00,500,250,5,'шт'),(18,'Металлическая крестовина для офисных кресел',5,2700.00,500,250,5,'шт'),(19,'Пластиковый комплект для стула',6,900.00,300,250,100,'шт'),(20,'Кромка ПВХ',6,35.80,1500,1000,100,'м');
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
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
