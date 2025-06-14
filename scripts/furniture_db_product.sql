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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id_product` int NOT NULL AUTO_INCREMENT,
  `name_product` varchar(325) DEFAULT NULL,
  `id_type_production` int DEFAULT NULL,
  `article` decimal(20,1) DEFAULT NULL,
  `min_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_product`),
  KEY `id_type_production` (`id_type_production`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`id_type_production`) REFERENCES `producttype` (`id_product_type`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Кресло детское цвет Белый и Розовый',1,3028272.0,15324.99),(2,'Кресло офисное цвет Черный',1,3018556.0,21443.99),(3,'Кресло эргономичное цвет Темно-коричневый  ',1,3549922.0,24760.00),(4,'Полка настольная',2,7028048.0,2670.89),(5,'Стеллаж для документов цвет Дуб светлый 854х445х2105 мм',3,5759324.0,24899.00),(6,'Стеллаж цвет Белый с ящиками 854х445х2105 мм',3,5259474.0,16150.00),(7,'Стеллаж цвет Орех 400х370х2000 мм',3,5118827.0,2860.00),(8,'Стол для ноутбука на металлокаркасе 800х600х123 мм',4,1029784.0,14690.00),(9,'Стол компьютерный 700х600х500 мм',4,1028248.0,4105.89),(10,'Стол компьютерный на металлокаркасе 1400х600х750 мм',4,1130981.0,13899.00),(11,'Стол письменный 1100x750x600 мм',4,1188827.0,5148.00),(12,'Стол письменный с тумбочкой 4 ящика 1100x750x600 мм',4,1029272.0,15325.00),(13,'Стол руководителя письменный цвет Венге 1600x800x764 мм',4,1016662.0,43500.90),(14,'Стол руководителя письменный цвет Орех темный 2300x1000x750 мм',4,1658953.0,132500.00),(15,'Тумба выкатная 3 ящика',5,6033136.0,3750.00),(16,'Тумба офисная для оргтехники',5,6115947.0,2450.00),(17,'Узкий пенал стеллаж 5 полок цвет Орех 364х326x2000 мм ',3,5559898.0,8348.00),(18,'Шкаф для книг 800x420x2000 мм',6,4159043.0,23390.99),(19,'Шкаф для одежды цвет Венге 602x420x2000 мм',6,4758375.0,12035.00),(20,'Шкаф-витрина 2 ящика 800x420x2000 мм',6,4588376.0,31991.00);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
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
