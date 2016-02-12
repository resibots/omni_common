# omni_kinematics

#### Here we keep the code for efficient computation of the kinematic models of our omnidirectional robots.

## Authors

- Author/Maintainer: Federico Allocati

## Available models

- **omnipointer_kinematics** : Kinematic model for the Omnipointer robot. 
- **omnigrasper_kinematics** : Kinematic model for the Omnigrasper robot (matches vrep).

## How to compile

### Dependencies

- [Eigen]: C++ Linear Algebra Library

### Compile and install

- cd to `omni_kinematics` folder
- Configure with `./waf configure --prefix=path_to_install`
- Compile with `./waf build`
- Install with `./waf install`

## How to use it in other projects

### Using the WAF build system

Copy the file `waf_tools/omni_kinematics.py` to the folder where your wscript is.

Then add the following line to your `options(opt)` method:

```python
opt.load('omni_kinematics')
```

And the following lines to your `configure(conf)` method:

```python
conf.load('omni_kinematics')
conf.check_omni_kinematics()
```

You can specify an additional parameter `required=True` in the `check_omni_kinematics` method, to force the configuration to fail is the library is not found.

## LICENSE

[CeCILL]

[Eigen]: http://eigen.tuxfamily.org/
[CeCILL]: http://www.cecill.info/index.en.html