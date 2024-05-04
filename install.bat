conda create -n ppgan python=3.7 
conda activate ppgan
conda install -y ffmpeg=4.0.2 -c conda-forge
python.exe -m pip install --upgrade pip  
pip install paddlepaddle-gpu==2.4.1
pip install --upgrade ppgan
pip install protobuf==3.20


