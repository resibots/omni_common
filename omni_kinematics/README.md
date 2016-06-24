# omni_kinematics

Here we keep the code for efficient computation of the forward kinematic models of our omnidirectional robots. The currently available models are:

- Omnigrasper, for Omnigrasper robot as in simulation (matches vrep)
- Omnipointer, for the real Omnigrasper robot, without the Versaball end effector

## Authors

- Author/Maintainer: Federico Allocati

## How to compile

### Dependencies

- [Eigen]: C++ Linear Algebra Library

### Compile and install

- cd to `omni_kinematics` folder
- Configure with `./waf configure --prefix=/path/to/install`
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

## License

[CeCILL]

[Eigen]: http://eigen.tuxfamily.org/
[CeCILL]: http://www.cecill.info/index.en.html