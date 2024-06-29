# data transform
python gen_poses.py --factors 4 --scenedir ./data/nerf_llff_data/lego_car_dense
# train
nohup python run_nerf.py --config configs/lego_car_dense.txt --i_print 50 --factor 4&
# test
python run_nerf.py --config configs/lego_car_dense.txt --ft_path ./logs/lego_car_dense/200000.tar --render_only