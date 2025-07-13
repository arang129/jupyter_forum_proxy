import setuptools

setuptools.setup(
    name="jupyter-control-proxy",
    version='0.0.1',
    url="https://gitlab.mpcdf.mpg.de/khr/jupyter-streamlit-proxy",
    author="Klaus Reuter",
    description="klaus.reuter@mpcdf.mpg.de",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'control = jupyter_control_proxy:setup_control_proxy',
        ]
    },
    package_data={
        'jupyter_control_proxy': ['icons/*'],
    },
)
