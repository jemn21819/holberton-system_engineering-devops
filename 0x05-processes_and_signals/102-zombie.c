#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program that creates 5 zombie processes.
 * Return: value of process of infinite while
 */
int main(void)
{
	int stat, i;
	pid_t zombie[5];

	for (i = 0; i < 5; i++)
	{
		zombie[i] = fork();
		if (zombie[i] == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	sleep(100);
	while (--i > 0)
		zombie[i] = wait(&stat);
	infinite_while();

	return (0);
}
