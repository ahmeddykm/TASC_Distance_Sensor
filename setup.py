from setuptools import find_packages, setup

package_name = 'tasc_technical_task'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ahmedykm',
    maintainer_email='ahmedykm@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'distance_publisher = tasc_technical_task.distance_publisher:main',
            'distance_subscriber = tasc_technical_task.distance_subscriber:main'
        ],
    },
)
