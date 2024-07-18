---
title: PCA9685 dimmer
categories: [Hardware, Relay]
tags: [relay, dimmer, i2c, PCA9685]

image:
  path: /assets/img/PCA9685-dimmer.webp
  src: /assets/img/PCA9685-dimmer.webp
  alt: 'PCA9685 header image'

device_address: '&lt;I2C Address&gt;,[I2C Bus] where the [I2C bus](/TerrariumPI/hardware#i2c-bus) is optional<br />Ex: `1,0x40`'
dimmer_frequency: 5000
device_url: https://custom-build-robots.com/electronic/raspberry-pi-led-dimmer-pca9685-servo-controller/8840?lang=en
---

## Information

You want to make a cool robot, maybe a hexapod walker, or maybe just a piece of art with a lot of moving parts. Or maybe you want to drive a lot of LEDs with precise PWM output. Then you realize that your micro-controller has a limited number of PWM outputs! What now? You could give up OR you could just get this handy PWM and Servo driver breakout.

When we saw this chip, we quickly realized what an excellent add-on this would be. Using only two pins, control 16 free-running PWM outputs! You can even chain up 62 breakouts to control up to 992 PWM outputs (which we would really like to see since it would be glorious)

{% include_relative _relay_detail.md %}
