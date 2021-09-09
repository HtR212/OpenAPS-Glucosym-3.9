# OpenAPS-Glucosym

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!--
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    -->
    <li><a href="#simulation-workflow">Simulation Workflow</a></li>
      <ul>
        <li><a href="#setting-up-glucosym">Setting up Glucosym</a></li>
        <li><a href="#initializing-and-running-openaps-closed-loop">Initializing and running OpenAPS closed loop</a></li>
        <li><a href="#collecting-output-data">Collecting output data</a></li>
      </ul>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project



<!-- ### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com) -->

<!-- GETTING STARTED -->
## Getting Started



### Prerequisites
Before the installation process, the following things need to be installed:
* python3.5   
* pip (``` $ wget https://bootstrap.pypa.io/pip/3.5/get-pip.py ```)   
* virtualenv@15.0.1 (``` $ pip install virtualenv==15.0.1 ```)  
* git   

### Installation

1. **Clone the repo**
  ```sh
  $ git clone https://github.com/HtR212/OpenAPS-Glucosym-3.git
  ```

2. **Virtual environment**   
  * A virtual environment need to be set up inside ./OpenAPS-Glucosym/:  
  ```sh
  $ cd ./OpenAPS-Glucosym-3  
  $ virtualenv --no-site-packages --python=/usr/bin/python3 ./venv/ #set up a virtual environment that uses python3.5  
  ```
  * To enter the virtual environment, use the following command:
  ```sh
  $ source ./venv/bin/activate
  ```
  * To quit the virtual environment, use the following command:
  ```sh
  (venv)$ deactivate
  ```
  * Note: The virtual environment needs to be activated while doing the following steps.
  
3. **Run the auto-install script**  
  ```sh
  (venv)$ chmod u+x ./closedloop3.5-setup.sh
  (venv)$ ./closedloop3.5-setup.sh
  ```
  
4. **Debug files under /bin**   
  Currently, there is not a better method to solve the bugs in files under /bin. So, these bugs need to be fixed manually. The first file to debug is /bin/openaps. In this file, change two print commands to Python3 syntax by adding a pair of parenthesis around the message to be printed and then change "except (OSError), e" to "except (OSError) as e". The second file to debug is /bin/openaps-report. In this file, delete "choices = choices.sort()" and change "choices = available.keys()" to "choices = sorted(available.keys())".
* After finishing the above steps, please close the current terminal window. 
   
<!-- SIMULATION WORKFLOW -->
## Simulation Workflow  

### Setting up Glucosym  

First, open a terminal window and run the following commands:  
```sh
(venv)$ cd ./OpenAPS-Glucosym-3
(venv)$ source ./venv/bin/activate
(venv)$ cd ./glucosym
(venv)$ npm start
```
Then, open a browser and navigate to http://localhost:3000.

### Initializing and running OpenAPS closed loop

Open another terminal window and initialize OpenAPS:
```sh
(venv)$ cd ./OpenAPS-Glucosym-3  
(venv)$ source ./venv/bin/activate
(venv)$ cd ./openaps3.5   
(venv)$ python initialize.py [initial bg]  
```
Next, change the initial bg of the selected patient on the glucosym server and run the closed loop simulation:
```sh
(venv)$ python updated_ct_script_iob_based.py [number of iterations]  
```

### Collecting output data
Run the following command:
```sh
(venv)$ python updated_collected.py
```
The output data should be collected in a file called data.scv under the OpenAPS directory.

<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->

<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request -->

<!-- LICENSE -->
<!-- ## License -->

<!-- Distributed under the MIT License. See `LICENSE` for more information. -->

<!-- CONTACT -->
<!-- ## Contact -->

<!--Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com -->

<!-- Project Link: [https://github.com/HtR212/OpenAPS-Glucosym](https://github.com/HtR212/OpenAPS-Glucosym) -->

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
<!-- * [GitHub Pages](https://pages.github.com) -->
