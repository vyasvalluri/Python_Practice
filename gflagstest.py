#!/usr/bin/env python3
import gflags
import sys



gflags.DEFINE_string('name', 'Mr. Vedavyas', 'you name')
gflags.DEFINE_integer('age', 1, 'your age in years', lower_bound=0)
gflags.DEFINE_boolean('debug', 'False', 'produces debug')
gflags.DEFINE_enum('job', 'running', ['running', 'stopped'], 'job status')
FLAGS = gflags.FLAGS

def main():
	if FLAGS.debug:
		print('non-flag arguments:')

	print('Happy Birthday ', FLAGS.name)
	if( FLAGS.age is not None):
		print('your are %d years old, and you job is %s ' %(FLAGS.age, FLAGS.job))

if __name__ == '__main__':
	gflags.FLAGS(sys.argv)
	main()