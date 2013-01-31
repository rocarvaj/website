# Submitting multiple jobs in Condor

- date: 2012-09-23 07:37
- category: work
- tags: tips, computing

------

A usual problem when running jobs in a cluster through the [Condor](http://research.cs.wisc.edu/condor/) job scheduler, is that it doesn't provide very flexible script-like functionality. In this post I propose a way to deal with a particular situation: Submitting a bunch of jobs with different arguments, in a batch.

This post assumes some familiarity with Condor. But I can tell you the short version: In Condor you create a "submitting" file (usually with extension .cmd) that looks something like this

    universe = vanilla
    executable = /path/to/my/executable
    arguments = arg1 arg2 arg3
    queue

Then, you submit this job to Condor with the command `condor_submit <nameOfCMDFile>`.

One way in which you can submit multiple jobs, is to change the arguments in the .cmd file and "queue" again:

    universe = vanilla
    executable = /path/to/my/executable
    arguments = arg1 arg2 arg3
    queue
    arguments = newArg1 newArg2 newArg3
    queue
    ...

This approach is not very elegant, specially if you have to submit 100 different jobs and they could change from time to time.

Another way of doing this is by using bash scripts. I use two script files (download them [here](https://gist.github.com/3770119)) to:

1. Generate multiple .cmd files, one for each instance (or argument) in an input file (`CMDMaker.sh`).
2. Submit the generated files to Condor, in a batch (`multiSubmit.sh`).

The files have comments with instructions. You may need to make these files executable after download, by using these commands in your terminal:

    chmod +x CMDMaker.sh
    chmod +x multiSubmit.sh

Enjoy!

**Note:** I'm pretty sure I got the idea for this solution from someone in the web. I'll try to find the reference to give proper credit.
