-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-11-2020 a las 03:49:25
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grupo_1_proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tasignatura`
--

CREATE TABLE `tasignatura` (
  `nIdAsignatura` int(11) NOT NULL,
  `nCodigo` varchar(10) NOT NULL,
  `cNombre` varchar(20) NOT NULL,
  `cRequisitos` varchar(50) NOT NULL,
  `nCreditos` int(10) NOT NULL,
  `nIntensidadHoraria` int(10) NOT NULL,
  `dCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tdocente`
--

CREATE TABLE `tdocente` (
  `nIdDocentes` int(11) NOT NULL,
  `cPrimerNombre` varchar(20) NOT NULL,
  `cSegundoNombre` varchar(20) DEFAULT NULL,
  `cPrimerApellido` varchar(20) NOT NULL,
  `cSegundoApellido` varchar(20) NOT NULL,
  `nEdad` int(100) NOT NULL,
  `nCedula` int(15) NOT NULL,
  `nTelefono` int(10) NOT NULL,
  `cCorreo` varchar(50) NOT NULL,
  `cTipoVia` varchar(10) NOT NULL,
  `cNumeroLetraVia` varchar(10) NOT NULL,
  `nViaUrbana` int(10) DEFAULT NULL,
  `cTipoViaGeneradora` varchar(10) NOT NULL,
  `nNumeroViaGeneradora` int(10) NOT NULL,
  `cSufijo` varchar(10) DEFAULT NULL,
  `nNumeroPlaca` int(10) NOT NULL,
  `cAdicional` varchar(10) DEFAULT NULL,
  `cEPS` varchar(50) NOT NULL,
  `cEdad` int(200) NOT NULL,
  `sexo` varchar(30) NOT NULL,
  `dCreacion` datetime NOT NULL,
  `nIdExperiencia` int(11) NOT NULL,
  `nIdAsignatura` int(11) NOT NULL,
  `nIdPrograma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `texperiencia`
--

CREATE TABLE `texperiencia` (
  `nIdExperiencia` int(11) NOT NULL,
  `nAnosExperiencia` int(10) NOT NULL,
  `cLugarDondeTrabajo` varchar(100) NOT NULL,
  `cTipoVia` varchar(10) NOT NULL,
  `cNumeroLetraVia` varchar(10) NOT NULL,
  `nViaUrbana` int(10) DEFAULT NULL,
  `cTipoViaGeneradora` varchar(10) NOT NULL,
  `nNumeroViaGeneradora` int(10) NOT NULL,
  `cSufijo` varchar(10) DEFAULT NULL,
  `nNumeroPlaca` int(10) NOT NULL,
  `cAdicional` varchar(10) DEFAULT NULL,
  `nTelefonoLugarTrabajo` int(10) NOT NULL,
  `cCorreoLugarTrabajo` varchar(30) NOT NULL,
  `cCargo` varchar(20) NOT NULL,
  `dCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `thistorial`
--

CREATE TABLE `thistorial` (
  `nIdHistorial` int(11) NOT NULL,
  `nCodigo` int(20) NOT NULL,
  `nIdReporte` int(11) NOT NULL,
  `dCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tperfil`
--

CREATE TABLE `tperfil` (
  `nIdPerfil` int(11) NOT NULL,
  `cNombrePerfil` varchar(20) NOT NULL,
  `cDecripcion` varchar(100) NOT NULL,
  `cMAcademico` int(11) NOT NULL,
  `cMUsuario` int(11) NOT NULL,
  `cMReporte` int(11) NOT NULL,
  `dCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tperfil`
--

INSERT INTO `tperfil` (`nIdPerfil`, `cNombrePerfil`, `cDecripcion`, `cMAcademico`, `cMUsuario`, `cMReporte`, `dCreacion`) VALUES
(1, 'diego', 'Tiene acceso a toda la base de datos', 1, 1, 1, '2020-11-16 21:46:18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tprograma`
--

CREATE TABLE `tprograma` (
  `nIdPrograma` int(11) NOT NULL,
  `nCodigoPrograma` int(20) NOT NULL,
  `cNombrePrograma` varchar(20) NOT NULL,
  `nIdAsignatura` int(11) NOT NULL,
  `nSemestre` int(10) NOT NULL,
  `dCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `treporte`
--

CREATE TABLE `treporte` (
  `nIdReporte` int(11) NOT NULL,
  `nCodigo` int(10) NOT NULL,
  `dReporte` datetime NOT NULL,
  `nIdDocentes` int(11) NOT NULL,
  `nIdAsignatura` int(11) NOT NULL,
  `nIdPrograma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tusuario`
--

CREATE TABLE `tusuario` (
  `nIdUsuario` int(11) NOT NULL,
  `cNombreUsuario` varchar(20) NOT NULL,
  `cContrasena` varchar(200) NOT NULL,
  `nIdPerfil` int(11) NOT NULL,
  `nCedula` int(15) NOT NULL,
  `nTelefono` int(20) NOT NULL,
  `cCorreo` varchar(50) NOT NULL,
  `nIdTipoUsuario` int(11) NOT NULL,
  `cTipoVia` varchar(10) NOT NULL,
  `cNumeroLetraVia` varchar(10) NOT NULL,
  `nViaUrbana` int(10) DEFAULT NULL,
  `cTipoViaGeneradora` varchar(10) NOT NULL,
  `nNumeroViaGeneradora` int(10) NOT NULL,
  `cSufijo` varchar(10) DEFAULT NULL,
  `nNumeroPlaca` int(10) NOT NULL,
  `cAdicional` varchar(10) DEFAULT NULL,
  `dCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tusuario`
--

INSERT INTO `tusuario` (`nIdUsuario`, `cNombreUsuario`, `cContrasena`, `nIdPerfil`, `nCedula`, `nTelefono`, `cCorreo`, `nIdTipoUsuario`, `cTipoVia`, `cNumeroLetraVia`, `nViaUrbana`, `cTipoViaGeneradora`, `nNumeroViaGeneradora`, `cSufijo`, `nNumeroPlaca`, `cAdicional`, `dCreacion`) VALUES
(1, 'diego', '12345', 1, 1000729591, 316879700, 'diegofe21605@gmail.com', 1, 'calle', '49', 78, 'diagonal', 106, 'no aplica', 95, 'r', '2020-11-16 21:46:55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `t_tipousuario`
--

CREATE TABLE `t_tipousuario` (
  `nIdTipoUsuario` int(11) NOT NULL,
  `cTipoUsuario` varchar(20) NOT NULL,
  `cDescripcion` varchar(100) NOT NULL,
  `dCreacion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `t_tipousuario`
--

INSERT INTO `t_tipousuario` (`nIdTipoUsuario`, `cTipoUsuario`, `cDescripcion`, `dCreacion`) VALUES
(1, 'Administrador', 'Tiene acceso a toda la base de datos', '2020-11-16 21:43:21'),
(2, 'Secretari@', 'Tiene un acceso mas restringido', '2020-11-16 21:44:26'),
(4, '', '', '0000-00-00 00:00:00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tasignatura`
--
ALTER TABLE `tasignatura`
  ADD PRIMARY KEY (`nIdAsignatura`),
  ADD UNIQUE KEY `nCodigo` (`nCodigo`);

--
-- Indices de la tabla `tdocente`
--
ALTER TABLE `tdocente`
  ADD PRIMARY KEY (`nIdDocentes`),
  ADD UNIQUE KEY `nCedula` (`nCedula`),
  ADD KEY `nIdExperiencia` (`nIdExperiencia`),
  ADD KEY `nIdAsignatura` (`nIdAsignatura`),
  ADD KEY `nIdPrograma` (`nIdPrograma`);

--
-- Indices de la tabla `texperiencia`
--
ALTER TABLE `texperiencia`
  ADD PRIMARY KEY (`nIdExperiencia`);

--
-- Indices de la tabla `thistorial`
--
ALTER TABLE `thistorial`
  ADD PRIMARY KEY (`nIdHistorial`),
  ADD UNIQUE KEY `nCodigo` (`nCodigo`),
  ADD KEY `nIdReporte` (`nIdReporte`);

--
-- Indices de la tabla `tperfil`
--
ALTER TABLE `tperfil`
  ADD PRIMARY KEY (`nIdPerfil`),
  ADD UNIQUE KEY `cNombrePerfil` (`cNombrePerfil`);

--
-- Indices de la tabla `tprograma`
--
ALTER TABLE `tprograma`
  ADD PRIMARY KEY (`nIdPrograma`),
  ADD UNIQUE KEY `nCodigoPrograma` (`nCodigoPrograma`),
  ADD KEY `nIdAsignatura` (`nIdAsignatura`);

--
-- Indices de la tabla `treporte`
--
ALTER TABLE `treporte`
  ADD PRIMARY KEY (`nIdReporte`),
  ADD UNIQUE KEY `nCodigo` (`nCodigo`),
  ADD KEY `nIdDocentes` (`nIdDocentes`),
  ADD KEY `nIdAsignatura` (`nIdAsignatura`),
  ADD KEY `nIdPrograma` (`nIdPrograma`);

--
-- Indices de la tabla `tusuario`
--
ALTER TABLE `tusuario`
  ADD PRIMARY KEY (`nIdUsuario`),
  ADD UNIQUE KEY `cNombreUsuario` (`cNombreUsuario`),
  ADD KEY `nIdPerfil` (`nIdPerfil`),
  ADD KEY `nIdTipoUsuario` (`nIdTipoUsuario`);

--
-- Indices de la tabla `t_tipousuario`
--
ALTER TABLE `t_tipousuario`
  ADD PRIMARY KEY (`nIdTipoUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tasignatura`
--
ALTER TABLE `tasignatura`
  MODIFY `nIdAsignatura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tdocente`
--
ALTER TABLE `tdocente`
  MODIFY `nIdDocentes` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `texperiencia`
--
ALTER TABLE `texperiencia`
  MODIFY `nIdExperiencia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `thistorial`
--
ALTER TABLE `thistorial`
  MODIFY `nIdHistorial` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tperfil`
--
ALTER TABLE `tperfil`
  MODIFY `nIdPerfil` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tprograma`
--
ALTER TABLE `tprograma`
  MODIFY `nIdPrograma` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `treporte`
--
ALTER TABLE `treporte`
  MODIFY `nIdReporte` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tusuario`
--
ALTER TABLE `tusuario`
  MODIFY `nIdUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `t_tipousuario`
--
ALTER TABLE `t_tipousuario`
  MODIFY `nIdTipoUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tdocente`
--
ALTER TABLE `tdocente`
  ADD CONSTRAINT `tdocente_ibfk_1` FOREIGN KEY (`nIdExperiencia`) REFERENCES `texperiencia` (`nIdExperiencia`),
  ADD CONSTRAINT `tdocente_ibfk_2` FOREIGN KEY (`nIdAsignatura`) REFERENCES `tasignatura` (`nIdAsignatura`),
  ADD CONSTRAINT `tdocente_ibfk_3` FOREIGN KEY (`nIdPrograma`) REFERENCES `tprograma` (`nIdPrograma`);

--
-- Filtros para la tabla `thistorial`
--
ALTER TABLE `thistorial`
  ADD CONSTRAINT `thistorial_ibfk_1` FOREIGN KEY (`nIdReporte`) REFERENCES `treporte` (`nIdReporte`);

--
-- Filtros para la tabla `tprograma`
--
ALTER TABLE `tprograma`
  ADD CONSTRAINT `tprograma_ibfk_1` FOREIGN KEY (`nIdAsignatura`) REFERENCES `tasignatura` (`nIdAsignatura`);

--
-- Filtros para la tabla `treporte`
--
ALTER TABLE `treporte`
  ADD CONSTRAINT `treporte_ibfk_1` FOREIGN KEY (`nIdDocentes`) REFERENCES `tdocente` (`nIdDocentes`),
  ADD CONSTRAINT `treporte_ibfk_2` FOREIGN KEY (`nIdAsignatura`) REFERENCES `tasignatura` (`nIdAsignatura`),
  ADD CONSTRAINT `treporte_ibfk_3` FOREIGN KEY (`nIdPrograma`) REFERENCES `tprograma` (`nIdPrograma`);

--
-- Filtros para la tabla `tusuario`
--
ALTER TABLE `tusuario`
  ADD CONSTRAINT `tusuario_ibfk_1` FOREIGN KEY (`nIdPerfil`) REFERENCES `tperfil` (`nIdPerfil`),
  ADD CONSTRAINT `tusuario_ibfk_2` FOREIGN KEY (`nIdTipoUsuario`) REFERENCES `t_tipousuario` (`nIdTipoUsuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
