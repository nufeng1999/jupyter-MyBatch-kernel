from setuptools import setup

setup(name='jupyter_MyBatch_kernel',
      version='0.0.1',
      description='Minimalistic Dos Batch kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyBatch-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyBatch-kernel/tarball/0.0.1',
      packages=['jupyter_MyBatch_kernel'],
      scripts=['jupyter_MyBatch_kernel/install_MyBatch_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'dos','cmd','Batch','bat'],
      include_package_data=True
      )
