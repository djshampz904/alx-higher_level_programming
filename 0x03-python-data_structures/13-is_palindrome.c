#include "main.h"
	
/**
 * is_palidrome - checks if a linked list is a palidrome
 * @head: pointer to the head pointer to the list
 * Return: integer
 */

int is_palidrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return NULL
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL || fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *curr = slow;
	listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = 
}
