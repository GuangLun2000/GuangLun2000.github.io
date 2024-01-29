---
layout: page
permalink: /blogs/IoE/index.html
title: IoE
---
## Research Notes for IoE Group

> Final update in: 2024/01/28

These research notes provide my thoughts and findings related to ongoing projects within the Cambridge IoE Group, led by Prof. Ozgur B. Akan. More information can be found here: [IoE Group](https://ioe.eng.cam.ac.uk/).

### Paper Reading

- Received Signal and Channel Parameter Estimation in Molecular Communications
- Internet of Everything (IoE) — From Molecules to the Universe *(Article)*
- What Really is ‘Molecule’ in Molecular Communications? The Quest for Physics of Particle-based Information Carriers

---

## Molecular Communications (1)

### Basic Information:

- Title: Received Signal and Channel Parameter Estimation in Molecular Communications
- Authors: O. Tansel Baydas, **Ozgur B. Akan**
- Keywords: Molecular Communication, Channel Modeling, Received Signal Estimation, Channel Parameter, Maximum Likelihood Estimation
- URLs: [Research Paper](https://arxiv.org/abs/2311.14621)

---

### Introduction:

This paper presents a novel model for molecular communication (MC) that incorporates a spherical transmitter and receiver with partial absorption, and proposes an optimization-based technique using particle swarm optimization (PSO) for accurate estimation of the received signal. The estimated channel model is then used for estimating channel parameters such as distance and diffusion coefficient using iterative maximum likelihood estimation (MLE), achieving consistent errors compared to the estimated Cramer-Rao Lower Bound (CLRB).

### Background:

Molecular communication (MC) is a crucial paradigm for the Internet of Bio-Nano Things (IoBNT) framework, which combines nanomachines and biological entities. However, existing receiver architectures in MC literature, such as passive or entirely absorbing configurations, have limitations in accurately representing the reception of molecules. Additionally, the estimation of channel parameters in MC channels, such as distance and diffusion coefficient, is also an important research area. Previous methods have used closed-form estimators or iterative MLE approaches, but they often oversimplify the analysis or assume unrealistic conditions.

Motivation: Given the limitations of existing receiver architectures and channel parameter estimation methods in MC, the authors propose a more realistic MC model with a partially absorbing spherical receiver and develop an optimization-based technique using PSO for accurate received signal estimation. They also apply iterative MLE for channel parameter estimation and compare the results with the estimated CLRB. This research aims to improve the accuracy and realism of MC models and estimation techniques, contributing to the development of MC systems in the IoBNT framework.

---

### Methods:

- **a. Theoretical basis of the study:**
  - The study focuses on the combination of nanomachines and biological entities within the Internet of Bio-Nano Things (IoBNT) framework. It explores the potential applications of this combination, such as nano biosensors and artificial cells. Molecular communication (MC) is identified as a crucial component in enabling these applications. MC utilizes molecules as information carriers, and the transmission of information is achieved by encoding molecules based on type or concentration. However, concentration-based MC is susceptible to inter-symbol interference (ISI) caused by the stochastic characteristics of Brownian motion. Therefore, accurately describing the reception of molecules is important for designing appropriate transceivers and techniques for an MC channel.
- **b. Technical route of the article (step by step):**
  1. The sampling process assumes independence among the observations and models them as Poisson random variables.
  2. The joint probability density function (PDF) of the receiver's observations is expressed using the impulse response.
  3. The log-likelihood function is maximized to estimate the channel parameters (d and D) using the Newton-Raphson Method.
  4. The estimation process is stopped when it becomes constant.

---

### Results:

- Experimental settings in detail:
  - The experimental results show that the values of the correction parameters (b1, b2, and b3) remain consistent across different input parameters (d, R, and D).
- Experimental results in detail:
  - The error values for the estimated number of received molecules are around 0.44 for most scenarios, indicating that the distance between the transmitter and receiver or the radius of the receiver does not significantly influence the estimation.
  - **Compared to previous findings, the model demonstrates a significantly reduced root mean square error (RMSE) in estimating the cumulative number of received molecules, with a five-fold decrease.**

<br>

---

## Internet of Everything (IoE)

### Basic Info:

- Title: **Internet of Everything (IoE) — From Molecules to the Universe**
- Authors: **Ozgur B. Akan**, Ergin Dinc, Murat Kuscu, Oktay Cetinkaya, and Bilgesu A. Bilgin
- Keywords: Internet of Things, Internet of Everything, IoXs, IoE framework, heterogeneous IoXs
- URLs: [Review Paper](https://ieeexplore.ieee.org/abstract/document/10121570)

---

### Introduction:

This paper explores the potential synergies and opportunities that may arise from the interactions between heterogeneous IoXs (Internet of Xs), enabling unprecedented applications beyond the current confines of IoT (Internet of Things). The authors propose the Internet of Everything (IoE) framework, which aims to link existing and future IoXs on a diverse scale ranging from molecules to the universe. They discuss potential IoE applications, challenges, and propose a layered network architecture for IoE.

### Background:

The Internet of Things (IoT) has seen significant advancements, but its specialization into non-interacting application domains (IoXs) limits its potential for cross-domain synergies. For example, the Internet of Vehicles (IoV) focuses on optimizing traffic flow, but lacks integration with other domains like industrial plants (IIoT) or agricultural fields (IoAT). This disconnection between IoXs hinders the exploration of opportunities and synergies that can generate higher value. To address this limitation, the authors propose the Internet of Everything (IoE) framework, inspired by the ubiquitous connectivity and heterogeneous networking characteristics of the universe. IoE aims to link existing and unconventional IoXs, such as the Internet of Nano Things (IoNT) and the Internet of People and Senses (IoPS), to enable seamless cyber-physical interfaces and unprecedented levels of control over nature. The authors aim to explore the potential synergies and opportunities that can be enabled by the interactions of heterogeneous IoXs within the IoE framework, and propose a layered network architecture and an IoE middleware to address the challenges of interoperability, scalability, and integration of autonomous things. The perspectives and proposals in this paper aim to inspire academia and industry to explore and innovate beyond the current boundaries of IoT.

----

### Review:

- **a. Theoretical basis of the study:**
  - The study focuses on the concept of the Internet of Everything (IoE) framework, which aims to connect and integrate various Internet of Xs (IoXs) to enable synergies and opportunities beyond the current confines of IoT. The inspiration for the IoE framework comes from the ubiquitous connectivity and heterogeneous networking characteristics of the universe.
- **b. Technical route of the article (step by step):**
  - The article explores different IoXs, such as Internet of Energy (IoEn), Internet of Vehicles (IoV), Internet of Industrial Things (IIoT), Internet of Agricultural Things (IoAT), Internet of Money (IoM), Internet of Nano Things (IoNT), and Internet of People and Senses (IoPS). It discusses their technologies, applications, and potential benefits.
  - The article specifically focuses on the Internet of Nano Things (IoNT) and its aim to interconnect nanomachines with conventional wireless networks. It highlights the need for research in developing channel models, nano-transceiver architectures, modulation/detection techniques, and communication protocols for reliable information transfer at the nanoscale.
  - The article also discusses the Internet of People and Senses (IoPS), which involves sharing human cognitive functionalities and senses through the internet. It mentions technologies like the Tactile Internet for real-time sharing of touch and actuation, as well as research towards digital communication of smell and taste. It acknowledges challenges in instrumentation and brain research that need to be addressed.
  - The Industrial Internet of Things (IIoT) is another focus of the article, which combines the internet with industrial machinery to optimize industrial processes. It mentions the hardware, software, and communication technologies involved, such as sensors, cloud computing, data analytics, and AI. It highlights benefits like real-time monitoring, predictive maintenance, and automation.
  - The Internet of Vehicles (IoV) is discussed as well, involving the integration of vehicles into the IoT domain. It mentions the aim of establishing a network of \smart\ vehicles that exchange information to improve traffic flow and minimize risks and energy consumption. It mentions technologies like wireless communication protocols, big data analytics, and AI.
  - The Internet of Money (IoM) is explored, which utilizes cryptocurrencies and blockchain technology for faster, more secure, and transparent transactions. It mentions the potential to revolutionize industries like e-commerce, automotive, and energy.
  - The Internet of Energy (IoEn) is discussed, aiming to create a decentralized and flexible energy grid using smart meters, actuators, and wireless sensor networks. It mentions challenges like supply-demand imbalances, renewable energy incorporation, and energy-efficient techniques.
  - The article briefly mentions the Internet of Space (IoSp), which involves communication satellites providing global connectivity. It mentions high-throughput satellites (HTSs) and small CSs deployed in low Earth orbit (LEO) to form massive constellations. It highlights the role of IoSp as the backbone of IoXs in areas lacking traditional communication infrastructure.

---

### Results:

- **PS: this is a review paper.**

<br>

---

## Molecular Communications (2)

### Basic Information:

- Title: What Really is ‘Molecule’ in Molecular Communications? The Quest for Physics of Particle-based Information Carriers
- Authors: Hanlin Xiao, Kamela Dokaj, **Ozgur B. Akan**
- Keywords: Molecular Communication, Internet of Bio-Nano Things, Bacteria Network, Molecular Motor, Synthetic Biology, Nanotechnology, Pheromone communication, DNA communication, Calcium signaling, Micro/Nanorobots
- URLs: [Review Paper](https://arxiv.org/abs/2311.16356)

### Introduction:

This paper explores the nature of the information molecules used in molecular communication, delving into their physical characteristics, communication systems, and potential applications. The authors aim to bridge the gap between theoretical research and real-world applications by providing a comprehensive survey of commonly used information molecules.

### Background:

Molecular communication is a novel communication paradigm that uses molecules as information carriers, offering advantages over traditional electromagnetic-wave-based communication. It has the potential for applications in nanoscale information transfer within the human body, such as targeted drug delivery and health monitoring. Despite the rapid development of the field, the nature of the information molecules themselves has often been overlooked in the existing literature. This paper aims to address this gap by focusing on the properties of information molecules and their impact on molecular communication systems. The authors provide a comprehensive survey to enhance our understanding of molecular communication and facilitate the transition from research to practical applications.

---

### Methods:

- a. Theoretical basis of the study:
  - The paper aims to provide a comprehensive survey of commonly used information molecules in molecular communication systems, examining their physical characteristics, communication systems, and potential applications.
- b. Technical route of the article (step by step):
  - The paper discusses different classes of information molecules used in the literature, including DNAs, magnetic nanoparticles, calcium ions, neurotransmitters, odor molecules, and others.
  - The physical characteristics of these molecules, such as mass, charge, magnetic susceptibility, dimensions, diffusivity, and biocompatibility, are examined.
  - The components of the communication channel, including transmitters, propagation channels, and receivers, are explored.
  - Different modulation methods are employed for each information molecule class.
  - Experimental testbeds and performance analysis are discussed to accelerate the development of molecular communication systems.

---

### Results:

- **a. Experimental settings in detail:**
  - The paper discusses the potential of DNA-based molecular communication for in-body scenarios, including cardiovascular and extracellular spaces, for tasks such as targeted drug delivery and health monitoring.
  - Superparamagnetic iron oxide nanoparticles (SPIONs) are explored for their potential applications in medical imaging, targeted drug delivery, and molecular communication.
  - The communication channel for calcium signaling is examined, including the propagation channel and the receiver.
  - The synaptic communication system, utilizing neurotransmitters, is discussed in terms of its components and modulation techniques.
  - Odor molecules are investigated as information carriers for macro-scale molecular communication.
- **Experimental results in detail:**
  - The diffusivity of spherical molecules through water can be calculated using the Stokes-Einstein relation.
  - DNA-based communication systems can achieve a data rate of up to 6 bit/s.
  - SPION-based communication systems have achieved a data rate of up to 6.34 bit/s.
  - Synaptic communication systems have achieved data rates of 66.6 bit/s in an in-vivo nervous communication channel.
  - Odor molecules have potential applications in swarm robotics, agricultural monitoring, underwater and in-mine communications, and olfactory bulb-related disease diagnosis.
- **PS: this is a review paper!**

<br>

---

> To be continued.
