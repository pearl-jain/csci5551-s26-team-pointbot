from setuptools import find_packages, setup

package_name = 'pointbot_rviz'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/pointbot_rviz_display.launch.py']),
        ('share/' + package_name + '/launch', ['launch/pointbot_rviz_test.launch.py']),
        ('share/' + package_name + '/rviz', ['rviz/pointbot.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='',
    maintainer_email='stang451@umn.edu',
    description='',
    license='',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'test_visualizer = pointbot_rviz.test_visualizer:main',
        ],
    },
)
