#include "lists.h"
#include<stdlib.h>
/**
 *insert_node - introduce a new node into a sorted list
 *@head: is the head node pointing to the beginning of the list
 *@number: is the value being introduce to the list
 *Return: Null if malloc fails, new node pointer if it succeeds
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *previous = NULL;
	listint_t *forward = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (forward != NULL && forward->n < number)
	{
		previous = forward;
		forward = forward->next;
	}

	new->next = forward;
	previous->next = new;
	return (new);
}
