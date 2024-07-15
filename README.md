# Fast-App-Quick AI Functionality
 
This is a repo dedictated to posting and exploring ways to create fast AI functionality using external or custom models. Each of these functionalities can be added onto existing applications or built into it's own application. 

All requirements are listed within the requirements.txt file located within the specific functionality folder as well as the dependencies. The requirements can be installed into a venv or on your local Python. For some functionalities, you may need PyTorch and Cuda Toolkit installed. 

Prerequisites for CUDA powered applications/functionality:
<ul>
 <li>Visual Studio 2019 or 2022 (install Visual Studio + the C++ Development Tools/Modules)</li>
 <li>Cuda Toolkit 11.7 or 11.8 </li>
 <li>PyTorch for Cuda 11.7 or 11.8</li>
</ul>

If you have any questions or inquiries, please email me at danielle.mlconsultant@gmail.com

***

How to Install CUDA & CUDA Enabled PyTorch: 

0. Install Python - It is recommended to at least have 3.9 - 3.12 (ensure that you don't immediately update Python to it's newest version above 3.12 as the CUDA Toolkit may not be compatible...yet).

1. Make sure your hardware is compatible with CUDA Toolkit. General rule of thumb is that if you have a NVIDIA GTX+ you should be able to at least install Cuda Toolkit.
Check here: https://developer.nvidia.com/cuda-gpus
Minimum recommended GPU Architecture: Ampere OR (for advanced users )multuple GPU setup/programming. 

2. Install Visual Studio 2019 or 2022. This MUST be installed before Cuda Toolkit, if this is not installed beforehand you will get an error during toolkit installation.
You MUST install the C++ Development Modules.
Official Download Page: https://visualstudio.microsoft.com/vs/

3. Install Cuda Toolkit (recommended atleast version 11.7)
Official Cuda Release Page: https://developer.nvidia.com/cuda-toolkit-archive

4. PIP install PyTorch (make sure that it is CUDA enabled) - Just as a reminder that you must have Python installed into your system in order to use the pip command on your terminal/command line. 
https://pytorch.org/ - ex. pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

5. Restart your system and you should have CUDA Toolkit installed into your system.
To check for successful CUDA installation, go to your programs (Apps > Installed Apps) amd search for CUDA. You should be able to see your CUDA Toolkit version installed.  

