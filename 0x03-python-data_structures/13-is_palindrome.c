#include "lists.h"
#include<stdlib.h>

listint_t *rev_list_order(listint_t **head)
{
	listint_t *tmp = NULL;
	listint_t *current, *upfront;

	current = upfront = *head;
	while (upfront != NULL)
	{
		upfront = upfront->next;
		current->next = tmp;
		tmp = current;
		current = upfront;
	}
	*head = tmp;
	return (tmp);
}

int is_palindrome(listint_t **head)
{
	listint_t *forward = *head;
	listint_t *current = *head;
	listint_t *second_half_listp, *first_half_listp;

	if (*head == NULL)
		return (1);

	while(forward->next != NULL && forward->next->next != NULL)
	{
		current = current->next;
		forward = forward->next->next;
	}
	second_half_listp = rev_list_order(&(current->next));
	first_half_listp = *head;

	while (second_half_listp != NULL && first_half_listp != NULL)
	{
		if (first_half_listp->n != second_half_listp->n)
			return (0);
		second_half_listp = second_half_listp->next;
		first_half_listp = first_half_listp->next;
	}
	return (1);
}
