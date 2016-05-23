Title: Using Modular Multiplicative Inverse
Date: 2016-05-16
Category: Algorithms
Authors: habeebq

I was looking at an algorithm somebody came up with, and it invovled an inverse modulo function. I had not come across this before so it really grabbed by attention as I tried to understand what it does.

This page on [Khans Academy](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses) seemed like a very useful introduction to the process.

In, short the multiplicative modular inverse `iA` of a number `A` for a modulo `C` is defined as

    (A * iA) mod C = 1

Sometimes the modular inverse does not exist though, both A and C need to be coprime.

The interesting thing about the modular inverse is that it returns a value within the range C that will be unique.

This allows it to be used as a hashing or an obfuscation method that can be implemented fairly cheaply.
