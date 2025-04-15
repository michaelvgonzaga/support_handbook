# Debugging Solr Issues on Pantheon (Layman's Guide)

###### Check the Drupal version

- Run drush status | grep version to confirm.
- Drupal 8/9/10 must use Solr v8. Drupal 7 uses Solr v3.

######  Check if Solr version is declared

- Run cat pantheon.yml | grep search\|version.

- If not declared and the site is Drupal 8/9/10, add search: { version: 8 } to pantheon.yml.

###### Verify Solr is actually running and reachable
- Run drush search-api-pantheon:diagnose (or drush sapd).

- If it fails, use a cURL command to ping Solr:
curl -ksE /certs/binding.pem "https://$PANTHEON_INDEX_HOST:$PANTHEON_INDEX_PORT/$PANTHEON_INDEX_PATH$PANTHEON_INDEX_CORE/admin/ping?wt=json" | jq -r '.status'

If the output is not "OK", Solr isn't reachable.

###### Check search module versions
drush pml --format=table --fields=display_name,status,version | grep "search_api_pantheon\|search_api_solr"

###### Make sure both modules are enabled and not outdated.

- Check if site content is indexed
- Run drush search-api:status or drush sapi-s.
- If not 100% indexed, run drush search-api:index -vvv.

###### Confirm Solr actually has the content
- Run:
curl -ksE /certs/binding.pem "https://$PANTHEON_INDEX_HOST:$PANTHEON_INDEX_PORT/$PANTHEON_INDEX_PATH$PANTHEON_INDEX_CORE/select?q=*:*" | jq -r '.response.numFound'
- Compare result count with CMS index count.

###### Check for Solr schema mismatches

- Run:
curl -ksE /certs/binding.pem "https://$PANTHEON_INDEX_HOST:$PANTHEON_INDEX_PORT/$PANTHEON_INDEX_PATH$PANTHEON_INDEX_CORE/schema?wt=json" | jq -r '.schema.name'
Compare this with the expected schema from the installed module.

###### If schema is outdated

- Instruct customer to repost schema via the admin UI or Drush:
drush search-api-pantheon:postSchema pantheon_solr8 /code/web/modules/contrib/search_api_solr/jump-start/solr8/config-set/ -vvv
Reload Solr (if needed)

- Run:
drush solr-reload pantheon_solr8