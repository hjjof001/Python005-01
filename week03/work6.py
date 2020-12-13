'''
CREATE TABLE `user2` (
  `id` char(4) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `user2` VALUES ('1001', '张三');
INSERT INTO `user2` VALUES ('1002', '李四');


CREATE TABLE `Account` (
  `id` char(4) NOT NULL,
  `money` double(9,3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `zichan` VALUES ('1001', '1100.120');
INSERT INTO `zichan` VALUES ('1002', '604.060');


CREATE TABLE `audit` (
  `time` datetime DEFAULT NULL,
  `from_id` char(4) DEFAULT NULL,
  `to_id` char(4) DEFAULT NULL,
  `money` double(9,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''