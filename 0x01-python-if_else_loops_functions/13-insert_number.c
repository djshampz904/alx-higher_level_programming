#include "lists.h"

/**
 * insert_node - inserts node
 * @head: pointer to the head pointer
 * @number: value to insert
 * Return: pointer or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev, *newNode;

	if (head == NULL)
		return (0);
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (0);

	newNode->n = number;
	curr = *head;
	while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	if (prev == NULL)
	{
		newNode->next = *head;
		*head = newNode;
	} else
	{
		prev->next = newNode;
		newNode->next = curr;
	}

	return (newNode);
}
