from setuptools import setup
import glob
import os

package_name = 'world_class_cam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param', glob.glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pw',
    maintainer_email='pw@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = world_class_cam.img_publisher:main',
            'img_control = world_class_cam.img_control:main',
            'optical_flow = world_class_cam.optical_flow:main',
            'img_canny = world_class_cam.img_canny:main',      
            'img_mosaic = world_class_cam.img_mosaic:main',   
            'img_saturation = world_class_cam.img_saturation:main',
            'img_filtered_status = world_class_cam.img_filtered_status:main',
            'img_screenshot = world_class_cam.img_screenshot:main',
            'record_video = world_class_cam.record_video:main'
        ],
    },
)
