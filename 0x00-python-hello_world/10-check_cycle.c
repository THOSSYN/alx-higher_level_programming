#include "lists.h"
#include<stdio.h>

/**
 *check_cycle - checks if there is a loop in
 *linked list
 *@list: Is the head node of the list
 *Return: 1 if cycle exist, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
