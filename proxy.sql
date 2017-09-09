SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `proxy`
--
CREATE DATABASE IF NOT EXISTS `proxy` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `proxy`;

-- --------------------------------------------------------

--
-- 表的结构 `xb_proxy`
--

CREATE TABLE `xb_proxy` (
  `iphash` char(32) NOT NULL COMMENT 'ip的MD5值',
  `ip` varchar(255) DEFAULT NULL,
  `port` int(11) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `opacity` varchar(60) DEFAULT NULL,
  `protocol` varchar(255) DEFAULT NULL,
  `ttl` varchar(255) CHARACTER SET utf32 DEFAULT NULL,
  `delay` decimal(10,4) NOT NULL DEFAULT '0.0000',
  `speed` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '速度 kb/s',
  `verify_time` int(10) NOT NULL DEFAULT '0' COMMENT '验证时间',
  `crawl_time` int(10) NOT NULL DEFAULT '0',
  `source` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='代理ip';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `xb_proxy`
--
ALTER TABLE `xb_proxy`
  ADD KEY `opacity` (`opacity`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
