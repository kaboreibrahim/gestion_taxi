-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 02 oct. 2024 à 00:03
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.1.25

START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gestion-taxi`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add fournisseurs', 6, 'add_fournisseurs'),
(22, 'Can change fournisseurs', 6, 'change_fournisseurs'),
(23, 'Can delete fournisseurs', 6, 'delete_fournisseurs'),
(24, 'Can view fournisseurs', 6, 'view_fournisseurs'),
(25, 'Can add user', 7, 'add_proprietaire'),
(26, 'Can change user', 7, 'change_proprietaire'),
(27, 'Can delete user', 7, 'delete_proprietaire'),
(28, 'Can view user', 7, 'view_proprietaire'),
(29, 'Can add chauffeur', 8, 'add_chauffeur'),
(30, 'Can change chauffeur', 8, 'change_chauffeur'),
(31, 'Can delete chauffeur', 8, 'delete_chauffeur'),
(32, 'Can view chauffeur', 8, 'view_chauffeur'),
(33, 'Can add liaison vehicule chauffeur', 9, 'add_liaisonvehiculechauffeur'),
(34, 'Can change liaison vehicule chauffeur', 9, 'change_liaisonvehiculechauffeur'),
(35, 'Can delete liaison vehicule chauffeur', 9, 'delete_liaisonvehiculechauffeur'),
(36, 'Can view liaison vehicule chauffeur', 9, 'view_liaisonvehiculechauffeur'),
(37, 'Can add modele de voiture', 10, 'add_modeledevoiture'),
(38, 'Can change modele de voiture', 10, 'change_modeledevoiture'),
(39, 'Can delete modele de voiture', 10, 'delete_modeledevoiture'),
(40, 'Can view modele de voiture', 10, 'view_modeledevoiture'),
(41, 'Can add piece', 11, 'add_piece'),
(42, 'Can change piece', 11, 'change_piece'),
(43, 'Can delete piece', 11, 'delete_piece'),
(44, 'Can view piece', 11, 'view_piece'),
(45, 'Can add entree stock', 12, 'add_entreestock'),
(46, 'Can change entree stock', 12, 'change_entreestock'),
(47, 'Can delete entree stock', 12, 'delete_entreestock'),
(48, 'Can view entree stock', 12, 'view_entreestock'),
(49, 'Can add type de voiture', 13, 'add_typedevoiture'),
(50, 'Can change type de voiture', 13, 'change_typedevoiture'),
(51, 'Can delete type de voiture', 13, 'delete_typedevoiture'),
(52, 'Can view type de voiture', 13, 'view_typedevoiture'),
(53, 'Can add vehicule', 14, 'add_vehicule'),
(54, 'Can change vehicule', 14, 'change_vehicule'),
(55, 'Can delete vehicule', 14, 'delete_vehicule'),
(56, 'Can view vehicule', 14, 'view_vehicule'),
(57, 'Can add sortie stock', 15, 'add_sortiestock'),
(58, 'Can change sortie stock', 15, 'change_sortiestock'),
(59, 'Can delete sortie stock', 15, 'delete_sortiestock'),
(60, 'Can view sortie stock', 15, 'view_sortiestock'),
(61, 'Can add recette', 16, 'add_recette'),
(62, 'Can change recette', 16, 'change_recette'),
(63, 'Can delete recette', 16, 'delete_recette'),
(64, 'Can view recette', 16, 'view_recette'),
(65, 'Can add patente', 17, 'add_patente'),
(66, 'Can change patente', 17, 'change_patente'),
(67, 'Can delete patente', 17, 'delete_patente'),
(68, 'Can view patente', 17, 'view_patente'),
(69, 'Can add notebook', 18, 'add_notebook'),
(70, 'Can change notebook', 18, 'change_notebook'),
(71, 'Can delete notebook', 18, 'delete_notebook'),
(72, 'Can view notebook', 18, 'view_notebook'),
(73, 'Can add depense', 19, 'add_depense'),
(74, 'Can change depense', 19, 'change_depense'),
(75, 'Can delete depense', 19, 'delete_depense'),
(76, 'Can view depense', 19, 'view_depense'),
(77, 'Can add carte stationnement', 20, 'add_cartestationnement'),
(78, 'Can change carte stationnement', 20, 'change_cartestationnement'),
(79, 'Can delete carte stationnement', 20, 'delete_cartestationnement'),
(80, 'Can view carte stationnement', 20, 'view_cartestationnement'),
(81, 'Can add assurance', 21, 'add_assurance'),
(82, 'Can change assurance', 21, 'change_assurance'),
(83, 'Can delete assurance', 21, 'delete_assurance'),
(84, 'Can view assurance', 21, 'view_assurance'),
(85, 'Can add verification code', 22, 'add_verificationcode'),
(86, 'Can change verification code', 22, 'change_verificationcode'),
(87, 'Can delete verification code', 22, 'delete_verificationcode'),
(88, 'Can view verification code', 22, 'view_verificationcode'),
(89, 'Can add vidange', 23, 'add_vidange'),
(90, 'Can change vidange', 23, 'change_vidange'),
(91, 'Can delete vidange', 23, 'delete_vidange'),
(92, 'Can view vidange', 23, 'view_vidange'),
(93, 'Can add visite technique', 24, 'add_visitetechnique'),
(94, 'Can change visite technique', 24, 'change_visitetechnique'),
(95, 'Can delete visite technique', 24, 'delete_visitetechnique'),
(96, 'Can view visite technique', 24, 'view_visitetechnique');

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-08-14 22:00:35.723333', '1', 'kaboreousmane', 2, '[{\"changed\": {\"fields\": [\"Document\"]}}]', 7, 2),
(2, '2024-08-14 22:09:47.393318', '1', 'kaboreousmane', 2, '[{\"changed\": {\"fields\": [\"Photo\"]}}]', 7, 2),
(3, '2024-08-14 23:38:47.187070', '1c2051ac-a254-4a06-b225-41cde1f54ee3', 'CFAO', 1, '[{\"added\": {}}]', 6, 2),
(4, '2024-08-14 23:39:38.907446', '3a7ac6f8-c99a-474b-a62f-cd0e6ff663d0', 'SOCIDA', 1, '[{\"added\": {}}]', 6, 2),
(5, '2024-08-14 23:40:42.027456', '7b2b2421-743d-48d1-92b9-86b8d088fcdc', 'JOIN SPI    espresso', 1, '[{\"added\": {}}]', 11, 2),
(6, '2024-08-14 23:46:50.597129', '285de084-5eff-473b-b1ad-c9c438187943', 'Entrée de 10 JOIN SPI    espresso le 2024-08-14 23:46:50.461144+00:00', 1, '[{\"added\": {}}]', 12, 2),
(7, '2024-08-15 19:55:45.160046', '7b2b2421-743d-48d1-92b9-86b8d088fcdc', 'JOIN SPI    ESPRESSO ', 3, '', 11, 2),
(8, '2024-08-15 19:55:58.781040', 'ca007b94-50a7-45ce-a0db-588d60a76774', 'Notebook object (ca007b94-50a7-45ce-a0db-588d60a76774)', 3, '', 18, 2),
(9, '2024-08-15 19:55:58.935867', '8deb77c3-4ec9-484d-b9e9-a0c5fc2823e2', 'Notebook object (8deb77c3-4ec9-484d-b9e9-a0c5fc2823e2)', 3, '', 18, 2),
(10, '2024-08-15 19:55:59.136078', '8511fd41-ee5d-4457-ac8a-3cfa1c8fd80f', 'Notebook object (8511fd41-ee5d-4457-ac8a-3cfa1c8fd80f)', 3, '', 18, 2),
(11, '2024-08-15 19:55:59.200984', '419fa70c-5ceb-4bd1-897a-ca81613932e1', 'Notebook object (419fa70c-5ceb-4bd1-897a-ca81613932e1)', 3, '', 18, 2),
(12, '2024-08-15 19:55:59.256028', '38bf1ca6-d4c3-4b05-a528-45a4bd2b50d4', 'Notebook object (38bf1ca6-d4c3-4b05-a528-45a4bd2b50d4)', 3, '', 18, 2),
(13, '2024-08-15 20:32:48.638460', '4073d116-80dc-4850-bf25-4c50647fcd11', 'Notebook object (4073d116-80dc-4850-bf25-4c50647fcd11)', 1, '[{\"added\": {}}]', 18, 2),
(14, '2024-08-15 20:33:48.688167', '14096492-b020-4def-bb66-3bca8447f7df', 'Notebook object (14096492-b020-4def-bb66-3bca8447f7df)', 1, '[{\"added\": {}}]', 18, 2),
(15, '2024-08-18 15:09:15.545129', 'fabe9c74-b095-4b3d-8f9e-4d55cbdaaa54', 'Visite Technique - 0 -   1315WWCI', 3, '', 24, 2),
(16, '2024-08-18 15:09:15.748757', 'da8ffbb6-0e16-4a45-ba56-f89d73fd7c72', 'Visite Technique - 0 -   1063KS01', 3, '', 24, 2),
(17, '2024-08-18 15:09:15.830419', 'a5dd769e-d9e6-405f-a7a8-2c6e520c0311', 'Visite Technique - 0 -   1315WWCI', 3, '', 24, 2),
(18, '2024-08-18 15:09:15.899510', '775519df-5601-43bb-a021-8bbeb4378b35', 'Visite Technique - 0 -   1315WWCI', 3, '', 24, 2),
(19, '2024-08-18 15:09:16.168994', '70ac1592-defd-491f-a6ce-d80d76bf7bd5', 'Visite Technique - 0 -   1315WWCI', 3, '', 24, 2),
(20, '2024-08-18 15:09:16.269289', '6e88eba8-d7dc-4678-9b8e-85531aec55a4', 'Visite Technique - 0 -   1315WWCI', 3, '', 24, 2),
(21, '2024-08-18 15:09:16.352992', '5dd5c463-67ec-4bdc-a4ec-968610959713', 'Visite Technique - 0 -   1315WWCI', 3, '', 24, 2),
(22, '2024-08-18 15:09:16.469453', '08420741-9ad1-4d7b-8199-e91dd00c0fbd', 'Visite Technique - 0 -   1315WWCI', 3, '', 24, 2),
(23, '2024-08-18 18:20:14.036974', 'd96c2364-ca68-4eea-ad09-8dccdcce6af7', '   1160LX01', 3, '', 21, 2),
(24, '2024-08-18 18:20:14.302139', 'b56657e9-a119-4ead-bec3-333f4a808e2f', '   1160LX01', 3, '', 21, 2),
(25, '2024-08-18 18:20:14.364680', '8f779d73-1ef5-4ef3-bb28-d19f69f65637', '   1315WWCI', 3, '', 21, 2),
(26, '2024-08-18 18:20:14.549601', '87caaaa0-938f-4f15-ba6a-b1284e178f4f', '   1315WWCI', 3, '', 21, 2),
(27, '2024-08-18 18:20:14.702924', '7f6c6c86-15c3-46ad-939b-e24e4c3a9457', '   1315WWCI', 3, '', 21, 2),
(28, '2024-08-18 18:20:14.896935', 'afb055fa-4ef4-4b30-93cb-c6df5b679556', '   1063KS01', 3, '', 21, 2),
(29, '2024-08-18 18:20:14.981626', '1a74da13-b7f6-41ba-ba7c-367548c47ec8', '   1315WWCI', 3, '', 21, 2),
(30, '2024-08-18 18:20:15.320235', '332bc146-26a7-4c12-b839-c2be4f05b1d9', '   1315WWCI', 3, '', 21, 2),
(31, '2024-08-18 18:20:32.703858', '1b8b23a4-9772-498e-be89-45c3237e5efe', 'kone ben ', 3, '', 8, 2),
(32, '2024-08-18 18:20:53.278698', '2e0e9104-9f06-48d0-afb9-bb3cc8fb45ee', 'PLATEAU D\'EMBREYAGE    ESPRESSO - 25000CFA -   1063KS01', 3, '', 19, 2),
(33, '2024-08-18 18:21:04.368319', 'fb19013e-9390-4a17-965d-cc521189bf35', ' kone ben ', 3, '', 9, 2),
(34, '2024-08-18 18:22:35.319780', 'da1fb10a-f3f2-404c-b504-ccfeceb7c14d', '  1160LX01', 3, '', 14, 2),
(35, '2024-08-18 18:22:35.379796', 'b207fff7-afb0-4285-a560-7766318e50b8', '  1063KS01', 3, '', 14, 2),
(36, '2024-08-18 18:22:35.411042', '473b0c38-87c1-482e-9228-f6ed52b3c1d8', '  1315WWCI', 3, '', 14, 2),
(37, '2024-08-24 11:13:36.355374', 'e1ecb8ab-578a-454c-b66c-056996286293', '  1160LX01', 2, '[{\"changed\": {\"fields\": [\"Photo\"]}}]', 14, 2),
(38, '2024-08-24 11:30:32.840325', 'd0d4ed75-fe4d-47a7-a96d-cee4290c1c6b', 'casse abobo  ', 1, '[{\"added\": {}}]', 6, 2),
(39, '2024-08-24 11:31:00.926145', 'f7013308-9a88-469f-9042-635ac080130e', 'PLATEAU D\'EMBREYAGE    ESPRESSO ', 3, '', 11, 2),
(40, '2024-08-24 11:31:34.661339', '8e1ba0ee-9dcd-441b-9faf-aecf8e3ebb00', 'boite de vitesse    ESPRESSO ', 1, '[{\"added\": {}}]', 11, 2),
(41, '2024-08-24 12:47:54.459702', '43a664fe-58b0-4bdf-a26e-cf98023d8f72', 'Recette - 120000 CFA -   2206KN01', 3, '', 16, 2),
(42, '2024-08-24 12:47:54.940358', '43a664fe-58b0-4bdf-a26e-cf98023d8f72', 'Recette - 120000 CFA -   2206KN01', 3, '', 16, 2),
(43, '2024-09-13 21:55:54.382671', '6803e139-60ba-4515-8557-68d13dc058ef', 'MARUTI SUZUKI  ', 1, '[{\"added\": {}}]', 6, 2),
(44, '2024-09-13 22:04:24.092451', '46082abc-9e76-4ce6-bde5-b6b29816b03c', 'Notebook object (46082abc-9e76-4ce6-bde5-b6b29816b03c)', 2, '[{\"changed\": {\"fields\": [\"Piece\"]}}]', 18, 2),
(45, '2024-09-13 22:09:05.223868', '46082abc-9e76-4ce6-bde5-b6b29816b03c', 'Notebook object (46082abc-9e76-4ce6-bde5-b6b29816b03c)', 2, '[{\"changed\": {\"fields\": [\"Date sortie\"]}}]', 18, 2),
(46, '2024-09-13 22:09:42.455341', '46082abc-9e76-4ce6-bde5-b6b29816b03c', 'Notebook object (46082abc-9e76-4ce6-bde5-b6b29816b03c)', 2, '[{\"changed\": {\"fields\": [\"Date sortie\"]}}]', 18, 2),
(47, '2024-09-13 22:16:45.009712', '37cebc94-9021-4812-9ebf-6519e4faccf5', 'Notebook object (37cebc94-9021-4812-9ebf-6519e4faccf5)', 2, '[{\"changed\": {\"fields\": [\"Piece\"]}}]', 18, 2),
(48, '2024-09-13 22:22:42.102999', '37cebc94-9021-4812-9ebf-6519e4faccf5', 'Notebook object (37cebc94-9021-4812-9ebf-6519e4faccf5)', 2, '[{\"changed\": {\"fields\": [\"Piece\"]}}]', 18, 2),
(49, '2024-09-13 22:23:21.855753', '37cebc94-9021-4812-9ebf-6519e4faccf5', 'Notebook object (37cebc94-9021-4812-9ebf-6519e4faccf5)', 2, '[{\"changed\": {\"fields\": [\"Piece\"]}}]', 18, 2),
(50, '2024-09-13 22:23:45.830927', '369da18b-7e87-45a0-87c1-5a1627f2819e', 'Notebook object (369da18b-7e87-45a0-87c1-5a1627f2819e)', 2, '[{\"changed\": {\"fields\": [\"Piece\"]}}]', 18, 2),
(51, '2024-09-14 23:56:19.623472', 'ba6da51d-a6b5-40fa-966a-b7d907c1e88a', 'SHELL  ', 1, '[{\"added\": {}}]', 6, 2),
(52, '2024-09-14 23:56:24.448624', '083aa1ec-01bf-44af-9c50-86c4864ec79e', 'SHELL  ', 1, '[{\"added\": {}}]', 6, 2),
(53, '2024-09-14 23:56:24.743063', 'f215d227-0992-4e54-ab13-7cab431efe52', 'SHELL  ', 1, '[{\"added\": {}}]', 6, 2),
(54, '2024-09-14 23:56:35.055490', 'ba6da51d-a6b5-40fa-966a-b7d907c1e88a', 'SHELL  ', 3, '', 6, 2),
(55, '2024-09-14 23:56:35.287847', '083aa1ec-01bf-44af-9c50-86c4864ec79e', 'SHELL  ', 3, '', 6, 2),
(56, '2024-09-15 00:08:18.458696', '37cebc94-9021-4812-9ebf-6519e4faccf5', 'Notebook object (37cebc94-9021-4812-9ebf-6519e4faccf5)', 2, '[{\"changed\": {\"fields\": [\"Piece\", \"Kilometrage\"]}}]', 18, 2);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(21, 'taxi', 'assurance'),
(20, 'taxi', 'cartestationnement'),
(8, 'taxi', 'chauffeur'),
(19, 'taxi', 'depense'),
(12, 'taxi', 'entreestock'),
(6, 'taxi', 'fournisseurs'),
(9, 'taxi', 'liaisonvehiculechauffeur'),
(10, 'taxi', 'modeledevoiture'),
(18, 'taxi', 'notebook'),
(17, 'taxi', 'patente'),
(11, 'taxi', 'piece'),
(7, 'taxi', 'proprietaire'),
(16, 'taxi', 'recette'),
(15, 'taxi', 'sortiestock'),
(13, 'taxi', 'typedevoiture'),
(14, 'taxi', 'vehicule'),
(22, 'taxi', 'verificationcode'),
(23, 'taxi', 'vidange'),
(24, 'taxi', 'visitetechnique');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-14 21:29:31.453123'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-08-14 21:29:33.583316'),
(3, 'auth', '0001_initial', '2024-08-14 21:29:43.218307'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-08-14 21:29:45.152877'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-08-14 21:29:45.243345'),
(6, 'auth', '0004_alter_user_username_opts', '2024-08-14 21:29:45.612483'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-08-14 21:29:45.693271'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-08-14 21:29:45.779834'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-08-14 21:29:45.879108'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-08-14 21:29:45.952109'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-08-14 21:29:46.013027'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-08-14 21:29:46.483190'),
(13, 'auth', '0011_update_proxy_permissions', '2024-08-14 21:29:46.836198'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-08-14 21:29:46.947965'),
(15, 'taxi', '0001_initial', '2024-08-14 21:31:06.558897'),
(16, 'admin', '0001_initial', '2024-08-14 21:31:10.203156'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-08-14 21:31:10.348899'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-14 21:31:10.478702'),
(19, 'sessions', '0001_initial', '2024-08-14 21:31:11.523198'),
(20, 'taxi', '0002_alter_notebook_piece', '2024-08-14 21:31:11.663236'),
(21, 'taxi', '0003_depense_nom_du_founissuer', '2024-08-15 01:01:32.285780'),
(22, 'taxi', '0004_notebook_kilometrage', '2024-08-18 15:28:58.154224');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('03m6eeap3r1ynxogva1zsix4fj2ml9ns', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1seNjO:ifzYqs8194LTVwtoHlRkCRVi8LMbz-0yREgIfzfIjWg', '2024-08-28 23:48:42.449769'),
('26agz19uhkbjmtmfzwc412bnk235i8p8', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1shqSv:m77_Z4BRUAvjjunFNKsoNxqPX1Pg2dpYdj9SQTLCB5Y', '2024-09-07 13:06:01.995565'),
('2e7najswkc01hj09t6tj6w8wypu4ifok', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1shc9I:SNGq3dOBc9Es7hxufnXpBqSYyLWFaitnY6WS8nvI5Do', '2024-09-06 21:48:48.925994'),
('3yjziyrdo5q87mdkjkeftcstrvh37vgo', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1shNQE:RccsUZTQYVb0WOM-4Uw4ri6M7P-LMDg4VG2tJA14fGw', '2024-09-06 06:05:18.324134'),
('6jgvtpjs7d8pl4mhxar9yucow8smqfmp', '.eJxVjDsOwyAQRO9CHSHE-gMp0-cMaNldgpMIJGNXVu4eW3KRTDnvzWwq4LrksDaZw8Tqqqy6_HYR6SXlAPzE8qiaalnmKepD0Sdt-l5Z3rfT_TvI2PK-HgU9cRQ2iWwXuU8DOdsbZ33yyUUEsuA6iyAO4p40DIAe0QjgmEB9vhhUOSA:1shogS:2PZYyaCQLcd1Bgprs3Ce-A3YHOpQvPto3Aa2Ksx0Mhk', '2024-09-07 11:11:52.940242'),
('7aajjorje3je1wrbut2yyc7bst39b6tv', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1shqZy:VoGrbOXSaZ0wgDlrbo9BDN-eghRRZBzQQporB0Vkifg', '2024-09-07 13:13:18.565997'),
('7yrralvo8afbtcjf581kcy0avb4hszkq', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1shbde:S3mKujJvia8gtvpGOSE21kJzJ4hZAsifFdVEMayU8FA', '2024-09-06 21:16:06.856875'),
('bsab8kxwpxbqnuo9gbwmpq53vjj05zcd', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1shqa0:3iWnGDsrD-8J-RCow6l4RGFx7opmy_n9yt_rM4Bh-b8', '2024-09-07 13:13:20.366244'),
('cqzhqca1cesq80z6ibrr590vyh4bddxq', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1skLZ4:7e3FG4aiRqjDWJGzjn5wXcVtmFD2304fA2QXNVltQQQ', '2024-09-14 10:42:42.907146'),
('gpd37vn0cfuav5deuyo6pi2hdb8cwrcm', '.eJxVjLkKAjEURf8ltQzJZHmJpWApVtbhZSPBWWAyA4L470aZQttzzr1PYnFbs91qXGwJ5EiAHH6ZQ3-P00es-CjdV-ysducRy3Bdbi2ccIyXOcThtA_-XjLW3C60o94YLrWTGoAFyiNLqWcSEoDE4IXToJjhSntFmeg5pcyICNq1RgJ5vQElYTh9:1suqKO:3ZGQNnlye5anMnrZ7jipWlzXrDJ7ZngWiqQtulilE88', '2024-10-13 09:34:56.368516'),
('gw0p8wqhffr9ks7bw7ie8muwhaxwc337', '.eJxVjDsOwyAQRO9CHSHE-gMp0-cMaNldgpMIJGNXVu4eW3KRTDnvzWwq4LrksDaZw8Tqqqy6_HYR6SXlAPzE8qiaalnmKepD0Sdt-l5Z3rfT_TvI2PK-HgU9cRQ2iWwXuU8DOdsbZ33yyUUEsuA6iyAO4p40DIAe0QjgmEB9vhhUOSA:1spEG3:aYEExXUROdAC3LpKrwgabS0Lt4c_h864zHh6NuuC5uo', '2024-09-27 21:55:15.362059'),
('jhcqnmlrgore8xlsgq7hhl7x5pn4emqr', 'e30:1seMGG:5eBQ0Rguqgem5BWyJU3FBqkDStI6XDzZexxAi9af-88', '2024-08-28 22:14:32.033210'),
('jm11jgbm3lq0gcpj5ud8meuav6nd5pwi', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1sehB6:bFjd0bKPjYBEgT_XbbafiEafJ2WB5IKdRHfTE6-sQ_c', '2024-08-29 20:34:36.523374'),
('pq9ya912gjg8t7wzayvkq97j8gjolit8', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1sfkYa:7sbzj9Y9AT-HDQ1fOK9-pNmr-JkxPctnNbMQvCMY61U', '2024-09-01 18:23:12.214734'),
('qxjvmgdja8rdoz1tp86fmxfg6gudxhu7', '.eJxVjMsKwjAQRf8laynJNMlEl4JLceU6zORBim2FpgVB_HerdKHbc-49T-FpmYtfapp8F8VBoNj9MqZwS-NHzPTomq_YWG1OA3X9Zbquw5GGdL7H1B-3w1-lUC1rgg1LZw0GVAllBoVo5J6kDaylY-UsZGSDptWRQAJosDkrp1qLiI7E6w0gSDiW:1spCfS:OfQ3dNM_zzGNXkGVVA3iYW6QTUA1-YNNAUxNEHH8Pro', '2024-09-27 20:13:22.392941'),
('sb0xj1dj3k1uf9pwherejb5zbngsffxp', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1slcHB:bAGI5wPpMlIv3Ypgh1zunb7fkG7RgUmCLB1BlScd91k', '2024-09-17 22:45:29.038584'),
('tvwdlkyaokw9f8ccot6qpaci89ghz8vn', 'e30:1seLiD:LRqgaKKMzeX8hxToQjuVWhJsG6iq7yioPnizxio9R7w', '2024-08-28 21:39:21.063480'),
('uni8maxt1yco97wky2huc9rr9dnx58db', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1seWpq:dPVLHAyLBcRPYnHuzIIvC2-C2tEGYaIdirdeXYD3aho', '2024-08-29 09:31:58.198471'),
('z27mtu3clbuq3exntldbw7ukqp2tys9n', '.eJxVjDsOwyAQRO9CHSHE-gMp0-cMaNldgpMIJGNXVu4eW3KRTDnvzWwq4LrksDaZw8Tqqqy6_HYR6SXlAPzE8qiaalnmKepD0Sdt-l5Z3rfT_TvI2PK-HgU9cRQ2iWwXuU8DOdsbZ33yyUUEsuA6iyAO4p40DIAe0QjgmEB9vhhUOSA:1sjEts:6aQYgPnVP5JhTAXys3P46sY2qpwctq9L4GoF_FdUN-k', '2024-09-11 09:23:36.284530'),
('z550orotr7e86820nqlxzi3eae5zrvsi', '.eJxVjMsKwjAQRf8layl5TZO4FFyKK9dhJklJsA9oWhDEf7dKF7o9597zZB7XJfu1ptmXyI7MsMMvIwz3NH7Ego_SfMXOanMesPTX-bYNRxzSZYqpP-2Hv0rGmrdEssJGq3kEcFpY0AYcBkWtElpyx2W0PJAi3SWAIB0JF0jyFg2iVB2x1xshpzl6:1sjEyW:xuPNpxc813eI2XGsAU1RO0ctOJ1kpOI88t3EkXGudr0', '2024-09-11 09:28:24.380880');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_assurance`
--

CREATE TABLE `taxi_assurance` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Label_assurance` int(11) NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `Date_debut` date NOT NULL,
  `Date_fin` date NOT NULL,
  `Assureur` varchar(255) NOT NULL,
  `Montant_Assurance` int(11) NOT NULL,
  `immatriculation_id` char(32) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_assurance`
--

INSERT INTO `taxi_assurance` (`deleted`, `deleted_by_cascade`, `id`, `Label_assurance`, `Date_ajout`, `Date_debut`, `Date_fin`, `Assureur`, `Montant_Assurance`, `immatriculation_id`) VALUES
(NULL, 0, '1f52aed9db424f58814daba3e3ba6134', 3, '2024-09-13 21:43:22.226712', '2024-09-15', '2024-10-14', 'MATCA', 44000, '44b0a27483324e73818442d129844e35'),
(NULL, 0, '3258960627024438873c5cb87b760639', 2, '2024-09-13 21:44:58.157327', '2024-09-16', '2024-10-15', 'MATCA', 44000, '48cef5823c174a4fabe53d680934ebfe'),
(NULL, 0, '32b70d36d13647a1ac9d1724ca395642', 1, '2024-08-31 11:09:32.750925', '2024-08-02', '2024-09-01', 'MATCA', 44000, 'e37f67a4a15f4e1387ea43d394efba8e'),
(NULL, 0, '378ca28ef8aa4e8aa7b3ae3956a5095a', 2, '2024-09-29 09:37:09.527195', '2024-09-24', '2024-10-23', 'MATCA', 44000, '6599dd8f2e984afd8d9e9b30def17887'),
(NULL, 0, '3e42fbd8e6ee443b90f384b24d5e34a1', 1, '2024-08-31 12:56:50.172130', '2024-08-08', '2024-09-07', 'MATCA', 44000, 'e1ecb8ab578a454cb66c056996286293'),
(NULL, 0, '4129b4a523314bf38ce08f7bceea7e2b', 2, '2024-09-13 21:39:35.159542', '2024-09-07', '2024-10-06', 'MATCA', 44000, '07c439938d524bbfbe55464158a14701'),
(NULL, 0, '53ce4b45f8fe45049092ff3962ad0a16', 1, '2024-08-31 13:00:32.505252', '2024-08-16', '2024-09-15', 'MATCA', 44000, '48cef5823c174a4fabe53d680934ebfe'),
(NULL, 0, '59a849665875412e917c16f7132a9b73', 2, '2024-09-13 21:38:41.014749', '2024-09-08', '2024-10-07', 'MATCA', 44000, 'a17d8bbddc544a229a82fc82c488d95f'),
(NULL, 0, '6b8967bc35444dafb40f47403c0213d7', 1, '2024-08-31 12:52:58.150214', '2024-08-09', '2024-09-05', 'MATCA', 44000, '16a0d9d03cb840fdbcc7f75ae9ad4079'),
(NULL, 0, '89817560f23c45d2aee423d0468a5eb2', 2, '2024-08-31 13:08:23.077147', '2024-09-02', '2024-10-01', 'MATCA', 44000, 'e37f67a4a15f4e1387ea43d394efba8e'),
(NULL, 0, '8b700f1d5f714a1482d73a913b8013b0', 2, '2024-09-13 21:37:50.448333', '2024-09-08', '2024-10-07', 'MATCA', 44000, 'e1ecb8ab578a454cb66c056996286293'),
(NULL, 0, '98a8c31a38ab4140b540aec3cbcab889', 1, '2024-08-31 12:44:48.537920', '2024-08-07', '2024-09-06', 'MATCA', 44000, '07c439938d524bbfbe55464158a14701'),
(NULL, 0, '9e3abbbb53db4202808a6dfaeddf7079', 1, '2024-08-31 12:58:52.617099', '2024-08-13', '2024-09-12', 'MATCA', 44000, '3a10f358115743f99beb1d8b2e6fd130'),
(NULL, 0, 'a842e757717944079205d09f8f3aa70f', 2, '2024-08-31 13:01:26.599699', '2024-08-15', '2024-09-14', 'MATCA', 44000, '44b0a27483324e73818442d129844e35'),
(NULL, 0, 'a9bc7e2a882a4f17a4c8f11119994b87', 1, '2024-08-31 11:10:31.380473', '2024-08-31', '2024-09-30', 'MATCA', 44000, '35a555c646ec49b18bba5a1661ea5a89'),
(NULL, 0, 'aaa0c982280d4840b8e85e8f65d7a3ba', 1, '2024-08-31 12:47:22.209306', '2024-08-08', '2024-09-07', 'MATCA', 44000, 'a17d8bbddc544a229a82fc82c488d95f'),
(NULL, 0, 'c71e8108f7cc4acbbaff36745b024cb2', 1, '2024-08-31 11:12:57.183478', '2024-08-27', '2024-09-26', 'MATCA', 44000, '5a3938556ab04be4bc9b2ea12586a8b9'),
(NULL, 0, 'c9ed801dda5e42c18045d2ccf2841351', 1, '2024-08-24 12:54:25.749991', '2024-08-15', '2024-09-14', 'MATCA', 44000, '44b0a27483324e73818442d129844e35'),
(NULL, 0, 'd3106bc223b94e07bfd247e359c4e75e', 2, '2024-09-13 21:40:45.169878', '2024-09-06', '2024-10-05', 'MATCA', 44000, '16a0d9d03cb840fdbcc7f75ae9ad4079'),
(NULL, 0, 'd8e6b378dce5470196fa15eff34d8ae7', 1, '2024-08-24 11:35:35.904702', '2024-08-24', '2024-09-23', 'MATCA', 44000, '6599dd8f2e984afd8d9e9b30def17887'),
(NULL, 0, 'e81ee0a9b44048b48450bc46ffbd09d6', 1, '2024-08-28 09:30:13.568591', '2024-08-29', '2024-09-28', 'MATCA', 44000, '01da98e74c19437dbf90ac084463b754'),
(NULL, 0, 'ed660644fb65428b9feaf57094becebe', 1, '2024-09-13 21:42:43.175466', '2024-09-12', '2024-10-11', 'MATCA', 44000, '01f131b2b79d44abb422d53a69494093'),
(NULL, 0, 'f0ddc5e960a146e59465e0ce96e3f0bc', 1, '2024-08-31 11:11:29.895164', '2024-09-01', '2024-09-30', 'MATCA', 44000, '1000512d714a41ba97ea77629df592b9');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_cartestationnement`
--

CREATE TABLE `taxi_cartestationnement` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Date_de_debut` date NOT NULL,
  `Date_de_fin` date NOT NULL,
  `Label_carte_stationnement` int(11) NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `immatriculation_id` char(32) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_chauffeur`
--

CREATE TABLE `taxi_chauffeur` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Nom` varchar(255) NOT NULL,
  `Prenom` varchar(255) NOT NULL,
  `N_permis` varchar(255) NOT NULL,
  `N_CNI_chauffeur` varchar(255) NOT NULL,
  `Chauffeur_CNI_photos` varchar(100) DEFAULT NULL,
  `Annee_anciennete` varchar(255) NOT NULL,
  `Contact` varchar(20) NOT NULL,
  `Lieu_de_residence` varchar(255) NOT NULL,
  `Chauffeur_photos` varchar(100) DEFAULT NULL,
  `Date_de_prise_service` date NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_depense`
--

CREATE TABLE `taxi_depense` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Montant` int(11) NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `Date_depense` date NOT NULL,
  `piece_id` char(32) NOT NULL,
  `immatriculation_id` char(32) NOT NULL,
  `Nom_du_Founissuer_id` char(32) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_depense`
--

INSERT INTO `taxi_depense` (`deleted`, `deleted_by_cascade`, `id`, `Montant`, `Date_ajout`, `Date_depense`, `piece_id`, `immatriculation_id`, `Nom_du_Founissuer_id`) VALUES
(NULL, 0, '050ec4a676ae40608d64e04c84d17d32', 30000, '2024-08-31 12:01:32.334677', '2024-08-31', 'af61582f9a7943ed8ecb7aa7fb4a77c4', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, '09bcf27e4b204b23ae46619a35a5041e', 25000, '2024-08-31 12:00:23.481962', '2024-08-31', 'ad254d20aaf34b9fa99a321252c19fb0', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, '17c0871bbaa74f6cb238b2f8ab3cb2c7', 25000, '2024-09-13 22:29:24.137678', '2024-09-11', 'ad254d20aaf34b9fa99a321252c19fb0', '01f131b2b79d44abb422d53a69494093', '6803e13960ba4515855768d13dc058ef'),
(NULL, 0, '23f37977bc77403fa443a37b14f9be8e', 200000, '2024-08-24 11:32:47.734233', '2024-08-21', '8e1ba0ee9dcd441b9fafaecf8e3ebb00', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, '25093b4bb59e471891d97373f30bee7b', 15000, '2024-08-31 11:59:44.581664', '2024-08-31', '9656619ac73144ada22a6ffadfbb366c', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, '4470ddb8b6524a0ba45550e832c183e2', 25000, '2024-09-15 00:04:59.108582', '2024-09-15', 'f039ea19e54b4ce1bd0bf1071cd312c3', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, '543e2b2f7ebf4df09bf121270a0078b0', 135000, '2024-08-31 11:59:00.680794', '2024-08-31', 'a614d3c52a3a40d789f7ac8fd6db3b7c', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, '602e0fc6ae7c46d5947268940d9f3efc', 272000, '2024-08-31 12:21:43.008702', '2024-08-08', '9e715a6072de4302b88cfb029737a035', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, '7d3974e20ac842c081f21db535dcf777', 25000, '2024-09-13 22:25:00.235235', '2024-09-11', 'f039ea19e54b4ce1bd0bf1071cd312c3', '01f131b2b79d44abb422d53a69494093', '6803e13960ba4515855768d13dc058ef'),
(NULL, 0, '7d5a405e5bb04033863d0d41948b27c8', 10000, '2024-09-14 23:59:26.134029', '2024-09-14', '8bfa473dd4324cf1b6adbbee6ddefbd0', '48cef5823c174a4fabe53d680934ebfe', 'f215d22709924e54ab137cab431efe52'),
(NULL, 0, '9b68d341346a48858028fa157be3576c', 25000, '2024-08-31 12:00:34.628444', '2024-08-31', 'f039ea19e54b4ce1bd0bf1071cd312c3', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, 'b3bec22af7364686ae6183df4cfcc7cb', 25000, '2024-09-15 00:03:21.308477', '2024-09-15', 'ad254d20aaf34b9fa99a321252c19fb0', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b'),
(NULL, 0, 'e9e1da97eafd4b4ba78efb6e7a9bccb3', 170000, '2024-09-13 22:39:09.195831', '2024-09-13', '6e1fcac688f94da4b2bf8c585e39645d', '48cef5823c174a4fabe53d680934ebfe', '6803e13960ba4515855768d13dc058ef'),
(NULL, 0, 'fc4c1976dbbc435fbc2e41835c004568', 20000, '2024-08-31 12:01:11.129578', '2024-08-29', 'e60f9897a26947f4b2f99d55fe71d308', '3a10f358115743f99beb1d8b2e6fd130', 'd0d4ed75fe4d47a7a96dcee4290c1c6b');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_entreestock`
--

CREATE TABLE `taxi_entreestock` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `date_entree` datetime(6) NOT NULL,
  `quantite` int(11) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL,
  `piece_id` char(32) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_entreestock`
--

INSERT INTO `taxi_entreestock` (`deleted`, `deleted_by_cascade`, `id`, `date_entree`, `quantite`, `proprietaire_id`, `piece_id`) VALUES
(NULL, 0, '1575a35fc2be458c981fa0516112fc29', '2024-08-31 11:22:02.311025', 4, 7, '9656619ac73144ada22a6ffadfbb366c'),
(NULL, 0, '5351904a08f740479c6d68a3dc7e83d4', '2024-08-31 11:23:59.723308', 3, 7, 'e60f9897a26947f4b2f99d55fe71d308'),
(NULL, 0, '830442ac2b7e477a8a52ed06967430dd', '2024-08-31 11:22:16.479398', 4, 7, 'd9f2f3e456634828b9c625ef1606b281');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_fournisseurs`
--

CREATE TABLE `taxi_fournisseurs` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Nom_Fournisseur` varchar(255) NOT NULL,
  `Telephone_Fournisseur` varchar(20) NOT NULL,
  `Localisation` varchar(50) NOT NULL,
  `Email_Fournisseur` varchar(50) DEFAULT NULL
) ;

--
-- Déchargement des données de la table `taxi_fournisseurs`
--

INSERT INTO `taxi_fournisseurs` (`deleted`, `deleted_by_cascade`, `id`, `Nom_Fournisseur`, `Telephone_Fournisseur`, `Localisation`, `Email_Fournisseur`) VALUES
('2024-09-14 23:56:35.699242', 0, '083aa1ec01bf44af9c5086c4864ec79e', 'SHELL', '0000000', '.', 'mail non spécifié'),
(NULL, 0, '1c2051aca2544a06b22541cde1f54ee3', 'CFAO', '+255 01 02 33 14 04', 'ZONE4', 'mail non spécifié'),
(NULL, 0, '3a7ac6f8c99a474ba62fcd0e6ff663d0', 'SOCIDA', '+255 07 05 02 22 41', 'RUE MARIE PIERRE CURIE', 'mail non spécifié'),
(NULL, 0, '6803e13960ba4515855768d13dc058ef', 'MARUTI SUZUKI', '0000000', '.', 'mail non spécifié'),
('2024-09-14 23:56:35.575825', 0, 'ba6da51da6b540fa966ab7d907c1e88a', 'SHELL', '0000000', '.', 'mail non spécifié'),
(NULL, 0, 'd0d4ed75fe4d47a7a96dcee4290c1c6b', 'casse abobo', '//', 'abobo', 'mail non spécifié'),
(NULL, 0, 'f215d22709924e54ab137cab431efe52', 'SHELL', '0000000', '.', 'mail non spécifié');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_liaisonvehiculechauffeur`
--

CREATE TABLE `taxi_liaisonvehiculechauffeur` (
  `id` char(32) NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `chauffeur_id` char(32) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL,
  `vehicule_id` char(32) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_modeledevoiture`
--

CREATE TABLE `taxi_modeledevoiture` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `Proprietaire_id` bigint(20) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_modeledevoiture`
--

INSERT INTO `taxi_modeledevoiture` (`deleted`, `deleted_by_cascade`, `id`, `nom`, `Proprietaire_id`) VALUES
(NULL, 0, '1379887ef02049fe9e4c2dc5213e9487', 'DZIRE', 7),
(NULL, 0, '23d087a9d9394c8d9cc4b5dc2c1cc398', 'ALTO', 7),
(NULL, 0, 'f9752620eaa54343bfb8e4783c2e62e3', 'ESPRESSO', 7);

-- --------------------------------------------------------

--
-- Structure de la table `taxi_notebook`
--

CREATE TABLE `taxi_notebook` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `date_arrivage` datetime(6) NOT NULL,
  `statut_vehicule` varchar(15) NOT NULL,
  `motif` varchar(50) NOT NULL,
  `commentaire` longtext NOT NULL,
  `date_sortie` datetime(6) DEFAULT NULL,
  `chauffeur_id` char(32) DEFAULT NULL,
  `vehicule_id` char(32) DEFAULT NULL,
  `Kilometrage` int(11) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_notebook`
--

INSERT INTO `taxi_notebook` (`deleted`, `deleted_by_cascade`, `id`, `date_arrivage`, `statut_vehicule`, `motif`, `commentaire`, `date_sortie`, `chauffeur_id`, `vehicule_id`, `Kilometrage`) VALUES
(NULL, 0, '369da18b7e8745a087c15a1627f2819e', '2024-09-13 22:20:12.740270', 'garage', 'visite_technique', 'la tôlerie est a faire', NULL, NULL, '3a10f358115743f99beb1d8b2e6fd130', 360000),
(NULL, 0, '37cebc94902148129ebf6519e4faccf5', '2024-09-13 22:14:50.556731', 'circulation', 'visite_technique', 'tôlerie n\'est pas refaire', '2024-09-15 00:01:34.000000', NULL, '48cef5823c174a4fabe53d680934ebfe', 388759),
(NULL, 0, '46082abc9e764ce6bde5b6b29816b03c', '2024-09-13 21:52:45.427759', 'circulation', 'visite_technique', 'la tôlerie n\'a pas été refaire', '2024-09-12 12:00:00.000000', NULL, '01f131b2b79d44abb422d53a69494093', 360117),
(NULL, 0, '855b520aea2943779d1f33a1f299125e', '2024-08-31 11:44:00.688460', 'garage', 'En_panne', 'probleme de piece', NULL, NULL, '5a3938556ab04be4bc9b2ea12586a8b9', 115244),
(NULL, 0, 'a92576697a2e4bb9afb46eff21691f1c', '2024-08-31 11:38:22.359892', 'circulation', 'En_panne', 'les 4 bougies changer', '2024-08-31 11:38:31.585542', NULL, '35a555c646ec49b18bba5a1661ea5a89', 175041),
(NULL, 0, 'cdb9597346764a11a9f6894cd8e7a76a', '2024-08-31 11:47:18.879400', 'circulation', 'En_panne', 'depuis plus de 1 mois au garage', '2024-09-03 22:57:16.738133', NULL, '3a10f358115743f99beb1d8b2e6fd130', 12222);

-- --------------------------------------------------------

--
-- Structure de la table `taxi_notebook_piece`
--

CREATE TABLE `taxi_notebook_piece` (
  `id` bigint(20) NOT NULL,
  `notebook_id` char(32) NOT NULL,
  `piece_id` char(32) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_notebook_piece`
--

INSERT INTO `taxi_notebook_piece` (`id`, `notebook_id`, `piece_id`) VALUES
(43, '369da18b7e8745a087c15a1627f2819e', '3af86dd52d4a45aab9969f1c19038ef3'),
(42, '369da18b7e8745a087c15a1627f2819e', '584a5b12834340e5b462db3f2c4f2bed'),
(45, '369da18b7e8745a087c15a1627f2819e', '8d06df35f29d404f803d0bd71cf9e312'),
(39, '369da18b7e8745a087c15a1627f2819e', 'e60f9897a26947f4b2f99d55fe71d308'),
(40, '369da18b7e8745a087c15a1627f2819e', 'f039ea19e54b4ce1bd0bf1071cd312c3'),
(41, '369da18b7e8745a087c15a1627f2819e', 'fa32e8b7f0414ef1957a523f02d22e03'),
(37, '37cebc94902148129ebf6519e4faccf5', '3af86dd52d4a45aab9969f1c19038ef3'),
(36, '37cebc94902148129ebf6519e4faccf5', '584a5b12834340e5b462db3f2c4f2bed'),
(34, '37cebc94902148129ebf6519e4faccf5', '6724a3462457475baeb12cbc8708ca50'),
(38, '37cebc94902148129ebf6519e4faccf5', '6e1fcac688f94da4b2bf8c585e39645d'),
(46, '37cebc94902148129ebf6519e4faccf5', '8bfa473dd4324cf1b6adbbee6ddefbd0'),
(33, '37cebc94902148129ebf6519e4faccf5', 'e60f9897a26947f4b2f99d55fe71d308'),
(35, '37cebc94902148129ebf6519e4faccf5', 'fa32e8b7f0414ef1957a523f02d22e03'),
(32, '46082abc9e764ce6bde5b6b29816b03c', '3af86dd52d4a45aab9969f1c19038ef3'),
(26, '46082abc9e764ce6bde5b6b29816b03c', '584a5b12834340e5b462db3f2c4f2bed'),
(31, '46082abc9e764ce6bde5b6b29816b03c', '6724a3462457475baeb12cbc8708ca50'),
(29, '46082abc9e764ce6bde5b6b29816b03c', 'ad254d20aaf34b9fa99a321252c19fb0'),
(27, '46082abc9e764ce6bde5b6b29816b03c', 'e60f9897a26947f4b2f99d55fe71d308'),
(28, '46082abc9e764ce6bde5b6b29816b03c', 'f039ea19e54b4ce1bd0bf1071cd312c3'),
(30, '46082abc9e764ce6bde5b6b29816b03c', 'fa32e8b7f0414ef1957a523f02d22e03'),
(19, 'a92576697a2e4bb9afb46eff21691f1c', 'd9f2f3e456634828b9c625ef1606b281'),
(20, 'cdb9597346764a11a9f6894cd8e7a76a', '8e1ba0ee9dcd441b9fafaecf8e3ebb00'),
(21, 'cdb9597346764a11a9f6894cd8e7a76a', 'a614d3c52a3a40d789f7ac8fd6db3b7c'),
(24, 'cdb9597346764a11a9f6894cd8e7a76a', 'ad254d20aaf34b9fa99a321252c19fb0'),
(25, 'cdb9597346764a11a9f6894cd8e7a76a', 'af61582f9a7943ed8ecb7aa7fb4a77c4'),
(22, 'cdb9597346764a11a9f6894cd8e7a76a', 'e60f9897a26947f4b2f99d55fe71d308'),
(23, 'cdb9597346764a11a9f6894cd8e7a76a', 'f039ea19e54b4ce1bd0bf1071cd312c3');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_patente`
--

CREATE TABLE `taxi_patente` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Label_patente` int(11) NOT NULL,
  `Date_debut` date NOT NULL,
  `Date_fin` date NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `immatriculation_id` char(32) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_piece`
--

CREATE TABLE `taxi_piece` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `nom_piece` varchar(255) NOT NULL,
  `ref_piece` varchar(255) NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `Nom_du_Founissuer_id` char(32) NOT NULL,
  `modele_de_voiture_id` char(32) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_piece`
--

INSERT INTO `taxi_piece` (`deleted`, `deleted_by_cascade`, `id`, `nom_piece`, `ref_piece`, `Date_ajout`, `Nom_du_Founissuer_id`, `modele_de_voiture_id`, `proprietaire_id`) VALUES
(NULL, 0, '0b44965dc2ff4d528996ddb576e113af', 'PLAQUETTE DE FRIEN', '///', '2024-09-13 22:03:05.369987', '6803e13960ba4515855768d13dc058ef', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, '2c4e604ee11e485985ff38f9bbd71e0c', 'HUILLE DE BOITE', 'Shell Spirax S2 G 80W-90', '2024-09-14 23:58:40.782840', 'f215d22709924e54ab137cab431efe52', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, '3af86dd52d4a45aab9969f1c19038ef3', 'ROULEMENT AVG', '43440M74L10', '2024-09-13 21:57:49.756389', '6803e13960ba4515855768d13dc058ef', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '446facb03f6445c18225c1d523ce4ddf', 'BATTERIE', '///', '2024-08-31 11:16:18.047873', '1c2051aca2544a06b22541cde1f54ee3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, '584a5b12834340e5b462db3f2c4f2bed', 'COURROIE D\'ALTERNATEUR', '///', '2024-08-31 11:55:01.833993', '1c2051aca2544a06b22541cde1f54ee3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '6724a3462457475baeb12cbc8708ca50', 'PLAQUETTE DE FRIEN', '///', '2024-09-13 22:02:55.708875', '6803e13960ba4515855768d13dc058ef', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '6e1fcac688f94da4b2bf8c585e39645d', 'CREMAILLERE', '///', '2024-09-13 22:15:38.018682', '6803e13960ba4515855768d13dc058ef', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '8bfa473dd4324cf1b6adbbee6ddefbd0', 'HUILLE DE BOITE', 'Shell Spirax S2 G 80W-90', '2024-09-14 23:58:34.388132', 'f215d22709924e54ab137cab431efe52', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '8d06df35f29d404f803d0bd71cf9e312', 'JOINT SPI DE BOITE', '///', '2024-09-13 22:21:53.015688', '3a7ac6f8c99a474ba62fcd0e6ff663d0', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '8e1ba0ee9dcd441b9fafaecf8e3ebb00', 'boite de vitesse', '////', '2024-08-24 11:31:34.328281', 'd0d4ed75fe4d47a7a96dcee4290c1c6b', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '9656619ac73144ada22a6ffadfbb366c', 'CABLE D\'EMBRAYAGE', '23710M62S01-000', '2024-08-31 11:15:36.397875', '1c2051aca2544a06b22541cde1f54ee3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '9e715a6072de4302b88cfb029737a035', 'autre', '///', '2024-08-31 12:20:33.850760', 'd0d4ed75fe4d47a7a96dcee4290c1c6b', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'a614d3c52a3a40d789f7ac8fd6db3b7c', 'POMPE A ESSENCE', '28619078', '2024-08-31 11:17:36.902454', 'd0d4ed75fe4d47a7a96dcee4290c1c6b', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'abaebf6fefff4699a84bafdc05532032', 'COURROIE D\'ALTERNATEUR', '///', '2024-08-31 11:54:54.152390', '1c2051aca2544a06b22541cde1f54ee3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, 'ad254d20aaf34b9fa99a321252c19fb0', 'AMORTISSEUR AVD', '41601M62S00', '2024-08-31 11:18:29.093805', '6803e13960ba4515855768d13dc058ef', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'af61582f9a7943ed8ecb7aa7fb4a77c4', 'BATTERIE', '////', '2024-08-31 11:42:10.159559', 'd0d4ed75fe4d47a7a96dcee4290c1c6b', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'c68601bb933745df845272d50d57c587', 'CABLE D\'EMBRAYAGE', '///', '2024-08-31 11:21:10.411049', '1c2051aca2544a06b22541cde1f54ee3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, 'd9f2f3e456634828b9c625ef1606b281', 'BOUGIE D\'ALLUMAGE', '09482M00636-000', '2024-08-31 11:20:23.853899', '3a7ac6f8c99a474ba62fcd0e6ff663d0', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, 'e60f9897a26947f4b2f99d55fe71d308', 'BOUGIE D\'ALLUMAGE', '09482M00609-000', '2024-08-31 11:19:51.617717', '3a7ac6f8c99a474ba62fcd0e6ff663d0', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'ee29c2bf0b3c4518afa531fe23b26fa2', 'DISQUE', '5513M66R00-000', '2024-08-31 11:56:08.632479', '1c2051aca2544a06b22541cde1f54ee3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'f039ea19e54b4ce1bd0bf1071cd312c3', 'AMORTISSEUR AVG', '41602M62S00', '2024-08-31 11:45:14.666150', '6803e13960ba4515855768d13dc058ef', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
('2024-08-24 11:31:01.211671', 0, 'f70133089a88469f9042635ac080130e', 'PLATEAU D\'EMBREYAGE', '22100M66R22-000', '2024-08-15 00:04:07.196400', '3a7ac6f8c99a474ba62fcd0e6ff663d0', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'fa32e8b7f0414ef1957a523f02d22e03', 'ROULEMENT AVD', '43440M74L10', '2024-09-13 21:57:37.759028', '6803e13960ba4515855768d13dc058ef', 'f9752620eaa54343bfb8e4783c2e62e3', 7);

-- --------------------------------------------------------

--
-- Structure de la table `taxi_proprietaire`
--

CREATE TABLE `taxi_proprietaire` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `N_CNI_proprietaire` varchar(255) NOT NULL,
  `Proprietaire_CNI_photos` varchar(100) DEFAULT NULL,
  `N_registre_commerce` varchar(255) NOT NULL,
  `Contact` varchar(20) NOT NULL,
  `Proprietaire_photos` varchar(100) DEFAULT NULL,
  `is_verified` tinyint(1) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_proprietaire`
--

INSERT INTO `taxi_proprietaire` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `deleted`, `deleted_by_cascade`, `N_CNI_proprietaire`, `Proprietaire_CNI_photos`, `N_registre_commerce`, `Contact`, `Proprietaire_photos`, `is_verified`) VALUES
(2, 'pbkdf2_sha256$720000$ZraLLK3yiR1E30fFVyRSpQ$f+LhpIX3Xz7OJuLGdsJ6MX1fxzUHXOMAOBC1gsYHN7Y=', '2024-09-29 09:30:52.400000', 1, 'admin', '', '', '', 1, 1, '2024-08-14 21:59:01.263147', NULL, 0, '', '', '', '', '', 0),
(7, 'pbkdf2_sha256$720000$LJERE6UVmUgK3P6J49w7pH$9guB5tPGRkG1qqozAd7NRpPVWb1Mr9r5o400cX6pZDY=', '2024-09-29 09:34:56.127114', 0, 'kaboreibrahim', 'kabore', 'ibrahim', 'ibrakdev@gmail.com', 0, 1, '2024-08-14 23:27:59.967262', NULL, 0, '14784744', 'Proprietaire_CNI_documents/5439465-conception-d-illustration-de-dessin-anime-de-voiture-_2SODBTQ.jpg', '14254145', '010233540', 'Proprietaire_photos/WhatsApp_Image_2024-05-13_à_12.24.08_3e949003.jpg', 1);

-- --------------------------------------------------------

--
-- Structure de la table `taxi_proprietaire_groups`
--

CREATE TABLE `taxi_proprietaire_groups` (
  `id` bigint(20) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_proprietaire_user_permissions`
--

CREATE TABLE `taxi_proprietaire_user_permissions` (
  `id` bigint(20) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_recette`
--

CREATE TABLE `taxi_recette` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `Montant` int(11) NOT NULL,
  `immatriculation_id` char(32) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_recette`
--

INSERT INTO `taxi_recette` (`deleted`, `deleted_by_cascade`, `id`, `Date_ajout`, `Montant`, `immatriculation_id`) VALUES
('2024-08-24 12:47:57.722172', 0, '43a664fe58b04bdfa26ecf98023d8f72', '2024-08-24 12:26:56.270252', 120000, '3a10f358115743f99beb1d8b2e6fd130'),
(NULL, 0, '7680260935924a31a866e858ab0d1c13', '2024-08-24 12:48:31.409566', 0, '01da98e74c19437dbf90ac084463b754');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_sortiestock`
--

CREATE TABLE `taxi_sortiestock` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `date_sortie` datetime(6) NOT NULL,
  `quantite` int(11) NOT NULL,
  `piece_id` char(32) NOT NULL,
  `proprietaire_id` bigint(20) NOT NULL,
  `vehicule_id` char(32) DEFAULT NULL
) ;

--
-- Déchargement des données de la table `taxi_sortiestock`
--

INSERT INTO `taxi_sortiestock` (`deleted`, `deleted_by_cascade`, `id`, `date_sortie`, `quantite`, `piece_id`, `proprietaire_id`, `vehicule_id`) VALUES
(NULL, 0, '0bb81ecb23dc4c4e9b05a0975c59f401', '2024-08-31 11:23:06.193315', 4, 'd9f2f3e456634828b9c625ef1606b281', 7, '35a555c646ec49b18bba5a1661ea5a89'),
(NULL, 0, 'b5d52211337641428b5cbfbe6220ab09', '2024-08-31 11:24:33.408501', 3, 'e60f9897a26947f4b2f99d55fe71d308', 7, '3a10f358115743f99beb1d8b2e6fd130');

-- --------------------------------------------------------

--
-- Structure de la table `taxi_typedevoiture`
--

CREATE TABLE `taxi_typedevoiture` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `Proprietaire_id` bigint(20) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_typedevoiture`
--

INSERT INTO `taxi_typedevoiture` (`deleted`, `deleted_by_cascade`, `id`, `nom`, `Proprietaire_id`) VALUES
(NULL, 0, '549d8779f79942d8950187d25b319eb3', 'SUZUKI', 7);

-- --------------------------------------------------------

--
-- Structure de la table `taxi_vehicule`
--

CREATE TABLE `taxi_vehicule` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `Date_mise_en_circulation` date NOT NULL,
  `immatriculation` varchar(255) NOT NULL,
  `Numero_chassis` varchar(255) NOT NULL,
  `Nbr_place` int(11) NOT NULL,
  `Couleur` varchar(255) NOT NULL,
  `vehicule_photos` varchar(100) DEFAULT NULL,
  `Label_voiture` int(11) NOT NULL,
  `Marque_voiture_id` char(32) NOT NULL,
  `Modele_voiture_id` char(32) NOT NULL,
  `Proprietaire_id` bigint(20) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_vehicule`
--

INSERT INTO `taxi_vehicule` (`deleted`, `deleted_by_cascade`, `id`, `Date_ajout`, `Date_mise_en_circulation`, `immatriculation`, `Numero_chassis`, `Nbr_place`, `Couleur`, `vehicule_photos`, `Label_voiture`, `Marque_voiture_id`, `Modele_voiture_id`, `Proprietaire_id`) VALUES
(NULL, 0, '01da98e74c19437dbf90ac084463b754', '2024-08-23 22:23:46.781986', '2021-06-07', '2203KN01', 'MA3RFL41S00236361', 5, 'ORANGE', 'Vehicule_photos/TAXI-ESPRESSO_Q94m4Wb.png', 10, '549d8779f79942d8950187d25b319eb3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '01f131b2b79d44abb422d53a69494093', '2024-08-23 19:41:39.806554', '2021-08-10', '1063KS01', 'MA3RFL41S00236310', 5, 'ORANGE', 'Vehicule_photos/TAXI-ESPRESSO_mVrpSCR.png', 8, '549d8779f79942d8950187d25b319eb3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '07c439938d524bbfbe55464158a14701', '2024-08-23 06:23:53.287858', '2023-03-30', '1161LX01', 'MBHCZF63S00340987', 5, 'ORANGE', 'Vehicule_photos/DZIRE_hBUok5t.jpg', 5, '549d8779f79942d8950187d25b319eb3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, '1000512d714a41ba97ea77629df592b9', '2024-08-24 10:54:49.848707', '2024-08-24', 'AA-920-FZ', '///', 5, 'ORANGE', 'Vehicule_photos/DZIRE_6c1TgSZ.jpg', 14, '549d8779f79942d8950187d25b319eb3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, '16a0d9d03cb840fdbcc7f75ae9ad4079', '2024-08-23 19:23:37.509740', '2021-09-20', '2196KT01', 'MA3RFL41S00274049', 5, 'ORANGE', 'Vehicule_photos/TAXI-ESPRESSO_p41hiDt.png', 6, '549d8779f79942d8950187d25b319eb3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '35a555c646ec49b18bba5a1661ea5a89', '2024-08-23 06:10:53.180391', '2024-01-22', 'AA-209-CF', 'MBHCZF63S00459911', 5, 'ORANGE', 'Vehicule_photos/DZIRE_HQbX66w.jpg', 3, '549d8779f79942d8950187d25b319eb3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, '3a10f358115743f99beb1d8b2e6fd130', '2024-08-23 19:29:27.564282', '2021-06-21', '2206KN01', 'MA3RFL41S00236330', 5, 'ORANGE', 'Vehicule_photos/TAXI-ESPRESSO_sBDkPWv.png', 7, '549d8779f79942d8950187d25b319eb3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '44b0a27483324e73818442d129844e35', '2024-08-23 06:15:00.272325', '2022-12-07', '1582LP01', 'MBHCZF63S00229308', 5, 'ORANGE', 'Vehicule_photos/DZIRE_L5RcciK.jpg', 4, '549d8779f79942d8950187d25b319eb3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, '48cef5823c174a4fabe53d680934ebfe', '2024-08-23 22:49:01.448368', '2021-01-22', '3231KG01', 'MA3RFL41S00176451', 5, 'ORANGE', 'Vehicule_photos/TAXI-ESPRESSO_gEcVB0v.png', 12, '549d8779f79942d8950187d25b319eb3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '5a3938556ab04be4bc9b2ea12586a8b9', '2024-08-23 22:37:57.255060', '2021-01-22', '3232KG01', 'MA3RFL41S00172889', 5, 'ORANGE', 'Vehicule_photos/TAXI-ESPRESSO_OQZBpNm.png', 11, '549d8779f79942d8950187d25b319eb3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, '6599dd8f2e984afd8d9e9b30def17887', '2024-08-23 23:00:04.561304', '2024-08-20', 'AA-119-HL-01', 'MBHCZF63SRG499111', 5, 'ORANGE', 'Vehicule_photos/DZIRE_Lk7NFpQ.jpg', 13, '549d8779f79942d8950187d25b319eb3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, 'a17d8bbddc544a229a82fc82c488d95f', '2024-08-23 22:07:18.789848', '2021-11-18', '3162KV01', 'MA3RFL41S00287362', 5, 'ORANGE', 'Vehicule_photos/TAXI-ESPRESSO_Zmvc9kF.png', 9, '549d8779f79942d8950187d25b319eb3', 'f9752620eaa54343bfb8e4783c2e62e3', 7),
(NULL, 0, 'e1ecb8ab578a454cb66c056996286293', '2024-08-22 22:54:37.164571', '2023-03-30', '1160LX01', 'MBHCZF63S00340820', 5, 'ORANGE', 'Vehicule_photos/DZIRE_HzdWAxM.jpg', 1, '549d8779f79942d8950187d25b319eb3', '1379887ef02049fe9e4c2dc5213e9487', 7),
(NULL, 0, 'e37f67a4a15f4e1387ea43d394efba8e', '2024-08-22 22:59:05.509019', '2022-07-19', '1429LG01', 'MBHCZF63S00187679', 5, 'ORANGE', 'Vehicule_photos/DZIRE.jpg', 2, '549d8779f79942d8950187d25b319eb3', '1379887ef02049fe9e4c2dc5213e9487', 7);

-- --------------------------------------------------------

--
-- Structure de la table `taxi_verificationcode`
--

CREATE TABLE `taxi_verificationcode` (
  `id` bigint(20) NOT NULL,
  `code` varchar(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_vidange`
--

CREATE TABLE `taxi_vidange` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Label_vidange` int(11) NOT NULL,
  `Filtre_a_huile` varchar(3) NOT NULL,
  `Filtre_a_air` varchar(3) NOT NULL,
  `Filtre_a_pollen` varchar(3) NOT NULL,
  `Filtre_a_gasoil` varchar(3) NOT NULL,
  `Kilometrage_vidange` int(11) NOT NULL,
  `Kilometrage_prochaine_vidange` int(11) NOT NULL,
  `Date_vidange` datetime(6) NOT NULL,
  `Observation` longtext NOT NULL,
  `Nom_chauffeur_id` char(32) NOT NULL,
  `immatriculation_id` char(32) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Structure de la table `taxi_visitetechnique`
--

CREATE TABLE `taxi_visitetechnique` (
  `deleted` datetime(6) DEFAULT NULL,
  `deleted_by_cascade` tinyint(1) NOT NULL,
  `id` char(32) NOT NULL,
  `Ref` int(11) NOT NULL,
  `Date_de_debut` date NOT NULL,
  `Date_de_fin` date NOT NULL,
  `Centre_agree` varchar(8) NOT NULL,
  `Vignette` varchar(3) NOT NULL,
  `Numero_vignette` varchar(20) DEFAULT NULL,
  `Montant` int(11) NOT NULL,
  `Observation` varchar(255) DEFAULT NULL,
  `Date_ajout` datetime(6) NOT NULL,
  `immatriculation_id` char(32) NOT NULL
) ;

--
-- Déchargement des données de la table `taxi_visitetechnique`
--

INSERT INTO `taxi_visitetechnique` (`deleted`, `deleted_by_cascade`, `id`, `Ref`, `Date_de_debut`, `Date_de_fin`, `Centre_agree`, `Vignette`, `Numero_vignette`, `Montant`, `Observation`, `Date_ajout`, `immatriculation_id`) VALUES
(NULL, 0, '063c529e4443473a90c7ae5ded468458', 0, '2024-02-14', '2025-02-16', 'SICTA', 'OUI', 'VRD2024146334', 55500, 'VGNR', '2024-09-14 07:36:57.339305', 'e37f67a4a15f4e1387ea43d394efba8e'),
(NULL, 0, '7fbc0ffedfc64178a0a010b050c0f213', 0, '2024-09-14', '2025-03-14', 'SICTA', 'NON', 'VRD2024126239', 20500, 'VGR', '2024-09-14 23:51:39.940865', '48cef5823c174a4fabe53d680934ebfe'),
(NULL, 0, 'b69113e2463549399cd1a456c9699ab2', 0, '2024-09-12', '2025-03-12', 'SICTA', 'OUI', 'VRD2024149476', 57500, 'VGNR', '2024-09-14 07:33:17.411297', '01f131b2b79d44abb422d53a69494093'),
(NULL, 0, 'f8b87d418dc84c639d76da7c632a5392', 0, '2024-08-23', '2025-02-23', 'SICTA', 'OUI', 'VRD20247090', 55500, 'VGNR', '2024-08-24 11:38:29.781544', '6599dd8f2e984afd8d9e9b30def17887');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_taxi_proprietaire_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `taxi_assurance`
--
ALTER TABLE `taxi_assurance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_assurance_immatriculation_id_54001b03_fk_taxi_vehicule_id` (`immatriculation_id`),
  ADD KEY `taxi_assurance_deleted_c616e82b` (`deleted`);

--
-- Index pour la table `taxi_cartestationnement`
--
ALTER TABLE `taxi_cartestationnement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_cartestationnem_immatriculation_id_8f131687_fk_taxi_vehi` (`immatriculation_id`),
  ADD KEY `taxi_cartestationnement_deleted_b0b872fb` (`deleted`);

--
-- Index pour la table `taxi_chauffeur`
--
ALTER TABLE `taxi_chauffeur`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_chauffeur_proprietaire_id_10fc4c46_fk_taxi_proprietaire_id` (`proprietaire_id`),
  ADD KEY `taxi_chauffeur_deleted_8b27aec6` (`deleted`);

--
-- Index pour la table `taxi_depense`
--
ALTER TABLE `taxi_depense`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_depense_piece_id_5cc3d2ee_fk_taxi_piece_id` (`piece_id`),
  ADD KEY `taxi_depense_immatriculation_id_afa31a06_fk_taxi_vehicule_id` (`immatriculation_id`),
  ADD KEY `taxi_depense_deleted_f03be574` (`deleted`),
  ADD KEY `taxi_depense_Nom_du_Founissuer_id_f62b503a_fk_taxi_four` (`Nom_du_Founissuer_id`);

--
-- Index pour la table `taxi_entreestock`
--
ALTER TABLE `taxi_entreestock`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_entreestock_proprietaire_id_170be4eb_fk_taxi_prop` (`proprietaire_id`),
  ADD KEY `taxi_entreestock_piece_id_3c8b199f_fk_taxi_piece_id` (`piece_id`),
  ADD KEY `taxi_entreestock_deleted_88c1aa46` (`deleted`);

--
-- Index pour la table `taxi_fournisseurs`
--
ALTER TABLE `taxi_fournisseurs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_fournisseurs_deleted_4df30269` (`deleted`);

--
-- Index pour la table `taxi_liaisonvehiculechauffeur`
--
ALTER TABLE `taxi_liaisonvehiculechauffeur`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_liaisonvehicule_vehicule_id_a73d7f4a_fk_taxi_vehi` (`vehicule_id`),
  ADD KEY `taxi_liaisonvehicule_chauffeur_id_d00722f2_fk_taxi_chau` (`chauffeur_id`),
  ADD KEY `taxi_liaisonvehicule_proprietaire_id_07e23180_fk_taxi_prop` (`proprietaire_id`);

--
-- Index pour la table `taxi_modeledevoiture`
--
ALTER TABLE `taxi_modeledevoiture`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_modeledevoiture_Proprietaire_id_ad994a39_fk_taxi_prop` (`Proprietaire_id`),
  ADD KEY `taxi_modeledevoiture_deleted_e2b30036` (`deleted`);

--
-- Index pour la table `taxi_notebook`
--
ALTER TABLE `taxi_notebook`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_notebook_chauffeur_id_135e620d_fk_taxi_liai` (`chauffeur_id`),
  ADD KEY `taxi_notebook_vehicule_id_fe59c908_fk_taxi_vehicule_id` (`vehicule_id`),
  ADD KEY `taxi_notebook_deleted_43d4f7b2` (`deleted`);

--
-- Index pour la table `taxi_notebook_piece`
--
ALTER TABLE `taxi_notebook_piece`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `taxi_notebook_piece_notebook_id_piece_id_9077f3c7_uniq` (`notebook_id`,`piece_id`),
  ADD KEY `taxi_notebook_piece_piece_id_ac23d56e_fk_taxi_piece_id` (`piece_id`);

--
-- Index pour la table `taxi_patente`
--
ALTER TABLE `taxi_patente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_patente_immatriculation_id_defa1168_fk_taxi_vehicule_id` (`immatriculation_id`),
  ADD KEY `taxi_patente_deleted_58c20c2c` (`deleted`);

--
-- Index pour la table `taxi_piece`
--
ALTER TABLE `taxi_piece`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_piece_Nom_du_Founissuer_id_ab400e37_fk_taxi_fournisseurs_id` (`Nom_du_Founissuer_id`),
  ADD KEY `taxi_piece_modele_de_voiture_id_acd1c182_fk_taxi_mode` (`modele_de_voiture_id`),
  ADD KEY `taxi_piece_proprietaire_id_df602eb8_fk_taxi_proprietaire_id` (`proprietaire_id`),
  ADD KEY `taxi_piece_deleted_472419f4` (`deleted`);

--
-- Index pour la table `taxi_proprietaire`
--
ALTER TABLE `taxi_proprietaire`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `taxi_proprietaire_deleted_278a2a32` (`deleted`);

--
-- Index pour la table `taxi_proprietaire_groups`
--
ALTER TABLE `taxi_proprietaire_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `taxi_proprietaire_groups_proprietaire_id_group_id_37bc4b99_uniq` (`proprietaire_id`,`group_id`),
  ADD KEY `taxi_proprietaire_groups_group_id_e49da224_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `taxi_proprietaire_user_permissions`
--
ALTER TABLE `taxi_proprietaire_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `taxi_proprietaire_user_p_proprietaire_id_permissi_e5ece7ec_uniq` (`proprietaire_id`,`permission_id`),
  ADD KEY `taxi_proprietaire_us_permission_id_34565b72_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `taxi_recette`
--
ALTER TABLE `taxi_recette`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_recette_immatriculation_id_d1edbac6_fk_taxi_vehicule_id` (`immatriculation_id`),
  ADD KEY `taxi_recette_deleted_0e19ec86` (`deleted`);

--
-- Index pour la table `taxi_sortiestock`
--
ALTER TABLE `taxi_sortiestock`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_sortiestock_piece_id_5fa2e612_fk_taxi_piece_id` (`piece_id`),
  ADD KEY `taxi_sortiestock_proprietaire_id_da2ce84c_fk_taxi_prop` (`proprietaire_id`),
  ADD KEY `taxi_sortiestock_vehicule_id_b05f54a3_fk_taxi_vehicule_id` (`vehicule_id`),
  ADD KEY `taxi_sortiestock_deleted_7e9ed3db` (`deleted`);

--
-- Index pour la table `taxi_typedevoiture`
--
ALTER TABLE `taxi_typedevoiture`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_typedevoiture_Proprietaire_id_9823c34c_fk_taxi_prop` (`Proprietaire_id`),
  ADD KEY `taxi_typedevoiture_deleted_1e30340c` (`deleted`);

--
-- Index pour la table `taxi_vehicule`
--
ALTER TABLE `taxi_vehicule`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `immatriculation` (`immatriculation`),
  ADD KEY `taxi_vehicule_Marque_voiture_id_90e9ae93_fk_taxi_type` (`Marque_voiture_id`),
  ADD KEY `taxi_vehicule_Modele_voiture_id_850e206f_fk_taxi_mode` (`Modele_voiture_id`),
  ADD KEY `taxi_vehicule_Proprietaire_id_ccf8ae79_fk_taxi_proprietaire_id` (`Proprietaire_id`),
  ADD KEY `taxi_vehicule_deleted_0404a555` (`deleted`);

--
-- Index pour la table `taxi_verificationcode`
--
ALTER TABLE `taxi_verificationcode`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `taxi_vidange`
--
ALTER TABLE `taxi_vidange`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_vidange_Nom_chauffeur_id_64eccc6b_fk_taxi_chauffeur_id` (`Nom_chauffeur_id`),
  ADD KEY `taxi_vidange_immatriculation_id_e4a087c8_fk_taxi_vehicule_id` (`immatriculation_id`),
  ADD KEY `taxi_vidange_deleted_758be46f` (`deleted`);

--
-- Index pour la table `taxi_visitetechnique`
--
ALTER TABLE `taxi_visitetechnique`
  ADD PRIMARY KEY (`id`),
  ADD KEY `taxi_visitetechnique_deleted_6f829190` (`deleted`),
  ADD KEY `taxi_visite_Date_de_9b304a_idx` (`Date_de_debut`),
  ADD KEY `taxi_visite_Date_de_9cc111_idx` (`Date_de_fin`),
  ADD KEY `taxi_visite_immatri_c22b85_idx` (`immatriculation_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `taxi_notebook_piece`
--
ALTER TABLE `taxi_notebook_piece`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `taxi_proprietaire`
--
ALTER TABLE `taxi_proprietaire`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `taxi_proprietaire_groups`
--
ALTER TABLE `taxi_proprietaire_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `taxi_proprietaire_user_permissions`
--
ALTER TABLE `taxi_proprietaire_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `taxi_verificationcode`
--
ALTER TABLE `taxi_verificationcode`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_taxi_proprietaire_id` FOREIGN KEY (`user_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_assurance`
--
ALTER TABLE `taxi_assurance`
  ADD CONSTRAINT `taxi_assurance_immatriculation_id_54001b03_fk_taxi_vehicule_id` FOREIGN KEY (`immatriculation_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_cartestationnement`
--
ALTER TABLE `taxi_cartestationnement`
  ADD CONSTRAINT `taxi_cartestationnem_immatriculation_id_8f131687_fk_taxi_vehi` FOREIGN KEY (`immatriculation_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_chauffeur`
--
ALTER TABLE `taxi_chauffeur`
  ADD CONSTRAINT `taxi_chauffeur_proprietaire_id_10fc4c46_fk_taxi_proprietaire_id` FOREIGN KEY (`proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_depense`
--
ALTER TABLE `taxi_depense`
  ADD CONSTRAINT `taxi_depense_Nom_du_Founissuer_id_f62b503a_fk_taxi_four` FOREIGN KEY (`Nom_du_Founissuer_id`) REFERENCES `taxi_fournisseurs` (`id`),
  ADD CONSTRAINT `taxi_depense_immatriculation_id_afa31a06_fk_taxi_vehicule_id` FOREIGN KEY (`immatriculation_id`) REFERENCES `taxi_vehicule` (`id`),
  ADD CONSTRAINT `taxi_depense_piece_id_5cc3d2ee_fk_taxi_piece_id` FOREIGN KEY (`piece_id`) REFERENCES `taxi_piece` (`id`);

--
-- Contraintes pour la table `taxi_entreestock`
--
ALTER TABLE `taxi_entreestock`
  ADD CONSTRAINT `taxi_entreestock_piece_id_3c8b199f_fk_taxi_piece_id` FOREIGN KEY (`piece_id`) REFERENCES `taxi_piece` (`id`),
  ADD CONSTRAINT `taxi_entreestock_proprietaire_id_170be4eb_fk_taxi_prop` FOREIGN KEY (`proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_liaisonvehiculechauffeur`
--
ALTER TABLE `taxi_liaisonvehiculechauffeur`
  ADD CONSTRAINT `taxi_liaisonvehicule_chauffeur_id_d00722f2_fk_taxi_chau` FOREIGN KEY (`chauffeur_id`) REFERENCES `taxi_chauffeur` (`id`),
  ADD CONSTRAINT `taxi_liaisonvehicule_proprietaire_id_07e23180_fk_taxi_prop` FOREIGN KEY (`proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`),
  ADD CONSTRAINT `taxi_liaisonvehicule_vehicule_id_a73d7f4a_fk_taxi_vehi` FOREIGN KEY (`vehicule_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_modeledevoiture`
--
ALTER TABLE `taxi_modeledevoiture`
  ADD CONSTRAINT `taxi_modeledevoiture_Proprietaire_id_ad994a39_fk_taxi_prop` FOREIGN KEY (`Proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_notebook`
--
ALTER TABLE `taxi_notebook`
  ADD CONSTRAINT `taxi_notebook_chauffeur_id_135e620d_fk_taxi_liai` FOREIGN KEY (`chauffeur_id`) REFERENCES `taxi_liaisonvehiculechauffeur` (`id`),
  ADD CONSTRAINT `taxi_notebook_vehicule_id_fe59c908_fk_taxi_vehicule_id` FOREIGN KEY (`vehicule_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_notebook_piece`
--
ALTER TABLE `taxi_notebook_piece`
  ADD CONSTRAINT `taxi_notebook_piece_notebook_id_a8549b79_fk_taxi_notebook_id` FOREIGN KEY (`notebook_id`) REFERENCES `taxi_notebook` (`id`),
  ADD CONSTRAINT `taxi_notebook_piece_piece_id_ac23d56e_fk_taxi_piece_id` FOREIGN KEY (`piece_id`) REFERENCES `taxi_piece` (`id`);

--
-- Contraintes pour la table `taxi_patente`
--
ALTER TABLE `taxi_patente`
  ADD CONSTRAINT `taxi_patente_immatriculation_id_defa1168_fk_taxi_vehicule_id` FOREIGN KEY (`immatriculation_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_piece`
--
ALTER TABLE `taxi_piece`
  ADD CONSTRAINT `taxi_piece_Nom_du_Founissuer_id_ab400e37_fk_taxi_fournisseurs_id` FOREIGN KEY (`Nom_du_Founissuer_id`) REFERENCES `taxi_fournisseurs` (`id`),
  ADD CONSTRAINT `taxi_piece_modele_de_voiture_id_acd1c182_fk_taxi_mode` FOREIGN KEY (`modele_de_voiture_id`) REFERENCES `taxi_modeledevoiture` (`id`),
  ADD CONSTRAINT `taxi_piece_proprietaire_id_df602eb8_fk_taxi_proprietaire_id` FOREIGN KEY (`proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_proprietaire_groups`
--
ALTER TABLE `taxi_proprietaire_groups`
  ADD CONSTRAINT `taxi_proprietaire_gr_proprietaire_id_ee7101f9_fk_taxi_prop` FOREIGN KEY (`proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`),
  ADD CONSTRAINT `taxi_proprietaire_groups_group_id_e49da224_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `taxi_proprietaire_user_permissions`
--
ALTER TABLE `taxi_proprietaire_user_permissions`
  ADD CONSTRAINT `taxi_proprietaire_us_permission_id_34565b72_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `taxi_proprietaire_us_proprietaire_id_a3f9fdfa_fk_taxi_prop` FOREIGN KEY (`proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_recette`
--
ALTER TABLE `taxi_recette`
  ADD CONSTRAINT `taxi_recette_immatriculation_id_d1edbac6_fk_taxi_vehicule_id` FOREIGN KEY (`immatriculation_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_sortiestock`
--
ALTER TABLE `taxi_sortiestock`
  ADD CONSTRAINT `taxi_sortiestock_piece_id_5fa2e612_fk_taxi_piece_id` FOREIGN KEY (`piece_id`) REFERENCES `taxi_piece` (`id`),
  ADD CONSTRAINT `taxi_sortiestock_proprietaire_id_da2ce84c_fk_taxi_prop` FOREIGN KEY (`proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`),
  ADD CONSTRAINT `taxi_sortiestock_vehicule_id_b05f54a3_fk_taxi_vehicule_id` FOREIGN KEY (`vehicule_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_typedevoiture`
--
ALTER TABLE `taxi_typedevoiture`
  ADD CONSTRAINT `taxi_typedevoiture_Proprietaire_id_9823c34c_fk_taxi_prop` FOREIGN KEY (`Proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_vehicule`
--
ALTER TABLE `taxi_vehicule`
  ADD CONSTRAINT `taxi_vehicule_Marque_voiture_id_90e9ae93_fk_taxi_type` FOREIGN KEY (`Marque_voiture_id`) REFERENCES `taxi_typedevoiture` (`id`),
  ADD CONSTRAINT `taxi_vehicule_Modele_voiture_id_850e206f_fk_taxi_mode` FOREIGN KEY (`Modele_voiture_id`) REFERENCES `taxi_modeledevoiture` (`id`),
  ADD CONSTRAINT `taxi_vehicule_Proprietaire_id_ccf8ae79_fk_taxi_proprietaire_id` FOREIGN KEY (`Proprietaire_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_verificationcode`
--
ALTER TABLE `taxi_verificationcode`
  ADD CONSTRAINT `taxi_verificationcode_user_id_f8dc1457_fk_taxi_proprietaire_id` FOREIGN KEY (`user_id`) REFERENCES `taxi_proprietaire` (`id`);

--
-- Contraintes pour la table `taxi_vidange`
--
ALTER TABLE `taxi_vidange`
  ADD CONSTRAINT `taxi_vidange_Nom_chauffeur_id_64eccc6b_fk_taxi_chauffeur_id` FOREIGN KEY (`Nom_chauffeur_id`) REFERENCES `taxi_chauffeur` (`id`),
  ADD CONSTRAINT `taxi_vidange_immatriculation_id_e4a087c8_fk_taxi_vehicule_id` FOREIGN KEY (`immatriculation_id`) REFERENCES `taxi_vehicule` (`id`);

--
-- Contraintes pour la table `taxi_visitetechnique`
--
ALTER TABLE `taxi_visitetechnique`
  ADD CONSTRAINT `taxi_visitetechnique_immatriculation_id_d27037a0_fk_taxi_vehi` FOREIGN KEY (`immatriculation_id`) REFERENCES `taxi_vehicule` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
