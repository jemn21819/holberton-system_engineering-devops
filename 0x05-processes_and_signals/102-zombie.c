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

int main(void)
{
	pid_t zombie;
	size_t i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie < 0)
			perror("fork");
		else if (zombie == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %ld\n",
					(long) zombie);
	}
	return (infinite_while());
}
